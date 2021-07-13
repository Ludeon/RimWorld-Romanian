#!/bin/python3.9

from pathlib import Path
import argparse
import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Union
from copy import deepcopy

RecDict = lambda: defaultdict(RecDict)

class TranslationStat:
    def __init__(self):
        self.t_todo = 0
        self.t_total = 0
        self.t_unused = 0
        self.w_todo = 0
        self.w_total = 0
        self.w_trans = 0
        self.w_script = 0

    def __add__(self, other):
        new = TranslationStat()
        new.t_todo   = self.t_todo   + other.t_todo
        new.t_total  = self.t_total  + other.t_total
        new.t_unused = self.t_unused + other.t_unused
        new.w_todo   = self.w_todo   + other.w_todo
        new.w_total  = self.w_total  + other.w_total
        new.w_trans  = self.w_trans  + other.w_trans
        new.w_script = self.w_script + other.w_script
        return new

    @property
    def w_pct(self):
        if self.w_total == 0:
            return 100.0
        return 100 - (self.w_todo / self.w_total) * 100

    @property
    def w_density(self):
        if self.t_total == 0:
            return 0
        return self.w_total / self.t_total

class TElement(ET.Element):
    @property
    def stats(self):
        stats = TranslationStat()
        last_comment = ET.Comment("")
        for elm in filter(lambda e: len(e) == 0, self.iter()):
            if elm.tag == ET.Comment:
                last_comment = elm
            elif elm.tag != ET.Comment and last_comment.text == " UNUSED ":
                stats.t_unused += 1
            elif elm.tag != ET.Comment:
                en_words = count_words(last_comment.text)
                stats.t_total += 1
                stats.w_total += en_words
                if is_script_tag(last_comment.text):
                    stats.w_script += en_words
                if elm.text == "TODO":
                    stats.t_todo += 1
                    stats.w_todo += en_words
                else:
                    stats.w_trans += count_words(elm.text)

        return stats

def is_script_tag(s: str) -> bool:
    return "<li>" in s

def count_words(s: str) -> int:
    if s is None:
        return 0
    words = s.strip().removeprefix("EN: ").split(" ")
    words = list(filter(lambda x: x != "", words))
    return len(words)

def load_xml(xmlPath: Path) -> ET:
    tBuilder = ET.TreeBuilder(element_factory=TElement, insert_comments=True)
    parser = ET.XMLParser(target=tBuilder, encoding="UTF-8")
    tree = ET.parse(str(xmlPath), parser)
    return tree

def save_xml(xmlPath: Path, tree: ET):
    xmlPath.parent.mkdir(parents=True, exist_ok=True)
    # NOTE: this will save as utf-8 without the BOM
    tree.write(str(xmlPath), encoding="utf-8", xml_declaration=True)

def load_xmls(rootPath) -> dict[str, Union[dict, "ElementTree"]]:
    xtree = defaultdict(RecDict)
    for xmlPath in args.input.rglob("*.xml"):
        parents = list(xmlPath.relative_to(rootPath).parents)[::-1][1:]
        parents = list(map(lambda x : x.name, parents))
        crt = xtree
        for p in parents:
            crt = crt[p]
        crt[xmlPath.stem] = load_xml(xmlPath)
    return xtree

def save_xmls(xtree, crtPath=Path(".")):
    if type(xtree) != defaultdict:
        crtPath = crtPath.with_suffix(".xml")
        save_xml(crtPath, xtree)
    else:
        for (k, v) in xtree.items():
            save_xmls(v, crtPath=crtPath/k)

def print_xtree(xtree, minWordThresh=None):
    def dfs(xtree, path=Path(".")):
        total_stats = TranslationStat()
        for (k, v) in xtree.items():
            if type(v) == ET.ElementTree:
                stats = v.getroot().stats
                total_stats += stats
                if minWordThresh is None or stats.w_total >= minWordThresh:
                    yield (v.getroot().stats, (path/k).with_suffix(".xml"))
            else:
                stats = yield from dfs(v, path/k)
                total_stats += stats
        yield (total_stats, path)
        return total_stats

    print("|%done|EN_words|w_density|w_script|Path|")
    print("|-:|-:|-:|-:|:-|")

    v = list(dfs(xtree))
    t = []
    for (s, path) in v:
        t.append([
            f"{s.w_pct:.2f}",
            s.w_total,
            f"{s.w_density:.0f}",
            str(s.w_script) if s.w_script > 0 else "",
            str(path)
        ])
    maxws = [0] * len(t[0])
    for line in t:
        for i, e in enumerate(line):
            slen = len(str(e))
            if maxws[i] < slen:
                maxws[i] = slen
    for line in t:
        for i, e in enumerate(line[:-1]):
            fmt = "|{:>%d}" % maxws[i]
            print(fmt.format(e), end="")
        print(f"|{line[-1]}|")


def parse_args():
    parser = argparse.ArgumentParser(description="t_stats - obtain statistics regarding translation progress")
    parser.add_argument("input", type=Path,
                        help="XML root to process (useful for specifying only indiviual folders)")
    parser.add_argument("-t", "--thresh", type=int, required=False, default=100,
                        help="Number of tags threshold under which to hide entries from being printed in the final stats")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    xtree = load_xmls(args.input)
    print_xtree(xtree, args.thresh)