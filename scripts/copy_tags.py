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
import pyperclip
import re

def get_filled_tags(root, force=False, filt=None, trans=False):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy/Insert tags to/from clipboard to XML file")
    parser.add_argument("file", type=Path,
                        help="Path to XML to be read/written to")
    parser.add_argument("-l", "--limit", type=int, default=4500,
                        help="Copy tags to clipboard only up to a certain limit")
    parser.add_argument("--force", action="store_const", default=False, const=True,
                        help="Ignore already-existing translations")
    parser.add_argument("-f", "--filter", type=str, required=False, default=None,
                        help="Filter selected tags by a regex")
    parser.add_argument("--translated", action="store_const", default=False, const=True,
                        help="Extract the already-translated tags, not the English reference")
    args = parser.parse_args()

    tBuilder = ET.TreeBuilder(insert_comments=True)
    parser = ET.XMLParser(target=tBuilder, encoding="UTF-8")
    og_tree = ET.parse(str(args.file), parser)


    filt = None
    if args.filter != None:
        filt = re.compile(args.filter)
    tags = get_filled_tags(og_tree.getroot(), force=args.force, filt=filt, trans=args.translated)
    num_tags = len(tags)
    crt_num = 0
    while len(tags) > 0:
        crt_tags = []

        # copy batch of tags to cliboard
        s = ""
        while len(s) < args.limit and tags:
            tag, txt = tags.pop()
            crt_tags.append(tag)
            s += f"#{tag.tag}\n{txt}\n\n"
        pyperclip.copy(s)
        print(f"Copied batch of {len(crt_tags)} to clipboard. Translate it via GT/deepl and press enter once ready...")

        # wait for the translated batch from clipboard
        lines = []
        while True:
            key = input("Press enter when ready, or 'q' to stop: ")
            if key.startswith("q"):
                break

            s = pyperclip.paste()
            lines = s.split("\n")
            lines = list(filter(lambda x : "#" not in x and len(x) > 0, lines))
            if len(lines) != len(crt_tags):
                print(f"mismatched input: found {len(lines)} (vs {len(crt_tags)} expected tags)")
                print(f"try again")
            else:
                break
        if key.startswith("q"):
            break

        # merge translations into loaded XML
        for (tag, trans) in zip(crt_tags, lines):
            tag.text = trans

        crt_num += len(crt_tags)
        print(f"{crt_num}/{num_tags} tags translated so far.")
        if len(tags) > 0:
            key = input("Continue with next batch? (y/n): ")
            if not key.startswith("y"):
                break

    # save data to disk
    print(f"Done translating {args.file}")
    key = "?"
    while key not in ["y", "n"]:
        key = input("Save contents to disk? (y/n): ")
    if key == "y":
        # NOTE: "UTF-8-sig" would save as utf-8 with the BOM, but rimworld does not accept that encoding for some reason
        og_tree.write(str(args.file), encoding="UTF-8", xml_declaration=True)