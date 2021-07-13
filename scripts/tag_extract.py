#!/bin/python3.9
#
#  Script that allows for:
#    - extracting untranslated tags from XMLS into a plaintext format
#    - inserting that plaintext format back into the XMLS
#
#  That plaintext format can be easily pasted into https://www.deepl.com for automated translation. This scipt allows
#  for computer-assised translation workflows, greatly increasing translation throughput.

from pathlib import Path
import argparse
import xml.etree.ElementTree as ET
from copy import copy
from typing import List, Tuple, Generator
import pyperclip
import re

def get_filled_tags(root, force=False, filt=None, trans=False) -> List[Tuple[ET.Element, str]]:
    last_comment = ET.Comment("")
    tags = []

    for elm in root:
        if elm.tag == ET.Comment:
            last_comment = elm
        elif len(elm) > 0:
            tags += get_filled_tags(elm, force=force, filt=filt, trans=trans)
        elif type(elm.tag) == str:
            if filt is None or filt.search(elm.tag):
                if trans:
                    if elm.text != "TODO" or force:
                        tags += [(elm, elm.text)]
                else:
                    if elm.text == "TODO" or force:
                        txt = last_comment.text.strip().removeprefix("EN: ")
                        tags += [(elm, txt)]
        else:
            raise Exception(f"What tf is this? {elm} {type(elm)}")

    return tags

class TagTextExtractor:
    def __init__(self, xmlPaths, args):
        self.xmlPaths = xmlPaths
        self.limit = args.limit
        self.force = args.force
        self.filter = args.filter
        self.trans = args.translated
        self.noComment = args.no_comment
        self.saveQueue = []

    def __empty_save_queue(self):
        for (t, p) in self.saveQueue:
            # NOTE: "UTF-8-sig" would save as utf-8 with the BOM, but rimworld does not accept that encoding for some reason
            t.write(str(p), encoding="UTF-8", xml_declaration=True)

    def get_mutable_tags(self):
        """
            Returns batches of mutable tags. After being modified, the changes in the tags will be reflected in the original file
        """
        crt_tags = []
        en_texts = []
        s = ""

        for xmlPath in self.xmlPaths:
            parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True), encoding="UTF-8")
            tree = ET.parse(str(xmlPath), parser)

            tag_count = 0
            for (tag, text) in get_filled_tags(tree.getroot(), force=self.force, filt=self.filter, trans=self.trans):
                tag_count += 1
                if self.noComment:
                    s_add = f"{text}\n\n"
                else:
                    s_add = f"#{tag.tag}\n{text}\n\n"

                if len(s) + len(s_add) > self.limit:
                    yield (crt_tags, en_texts, s)
                    self.__empty_save_queue()
                    crt_tags = []
                    en_texts = []
                    s = ""

                s += s_add
                crt_tags.append(tag)
                en_texts.append(text)

            if tag_count > 0:
                self.saveQueue.append((tree, xmlPath))

        if crt_tags:
            yield (crt_tags, en_texts, s)
            self.__empty_save_queue()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy/Insert tags to/from clipboard to XML file")
    parser.add_argument("file", type=Path, nargs="+", metavar="F",
                        help="Path to XML file (or folder of XMLs) to be read&written to")
    parser.add_argument("-l", "--limit", type=int, default=4500,
                        help="Copy tags to clipboard only up to a certain limit. Use 0 for no limit")
    parser.add_argument("--force", action="store_const", default=False, const=True,
                        help="Ignore already-existing translations")
    parser.add_argument("-f", "--filter", type=str, required=False, default=None,
                        help="Filter selected tags by a regex")
    parser.add_argument("--translated", action="store_const", default=False, const=True,
                        help="Extract the already-translated tags, not the English reference")
    parser.add_argument("--no-comment", action="store_const", default=False, const=True,
                        help="Do not add comments with the tagname")
    args = parser.parse_args()

    files = args.file
    dirs = list(filter(lambda x : x.is_dir(), files))
    files = [f for f in files if f not in dirs]
    for d in dirs:
        files += list(d.rglob("*.xml"))
    print(f"INFO: A total of {len(files)} files were provided")

    if args.filter != None:
        args.filter = re.compile(args.filter)

    extractor = TagTextExtractor(files, args)
    crt_num = 0
    abort = False
    for (tags, _, s) in extractor.get_mutable_tags():
        if abort:
            continue
        pyperclip.copy(s)
        print(f"Copied batch of {len(tags)} tags to clipboard. Translate it via GT/deepl and press enter once ready...")

        # wait for the translated batch from clipboard
        lines = []
        while True:
            key = input("Press enter when ready, or 'q' to stop: ")
            if key.startswith("q"):
                break

            s = pyperclip.paste()
            lines = s.split("\n")
            lines = list(filter(lambda x : "#" not in x and len(x) > 0 and "DeepL" not in x, lines))
            if len(lines) != len(tags):
                print(f"mismatched input: found {len(lines)} (vs {len(tags)} expected tags)")
                print(f"try again")
            else:
                break
        if key.startswith("q"):
            break

        # merge translations into loaded XML
        for (tag, trans_text) in zip(tags, lines):
            tag.text = trans_text

        crt_num += len(tags)
        print(f"{crt_num}/???? tags translated so far.")
        if len(tags) > 0:
            key = input("Continue with next batch? (y/n): ")
            if not key.startswith("y"):
                abort = True

    print(f"Done translating")