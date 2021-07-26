#!/bin/python3.9
from html.parser import HTMLParser
from pathlib import Path
import requests
import argparse
import itertools
from enum import Enum

"""
Example exerpt of response from www.pluralul.ro:

[...]
<div class=\'cont-list-title\'>Declinarea substantivului neutru mal:</div>
    <div class=\'table-responsive\'>
        <table class=\'table-declinare\' cellpadding=0 cellspacing=0>
            <tr>
                <th></th>
                <th colspan=2>Singular</th>
                <th colspan=2>Plural</th>
            </tr>
            <tr>
                <th>Caz</th>
                <th>Nearticulat</th>
                <th>Articulat</th>
                <th>Nearticulat</th>
                <th>Articulat</th>
            </tr>
            <tr>
                <th>Nominativ-Acuzativ</th>
                <td>mâl</td>
                <td>mâlul</td>
                <td>mâluri</td>
                <td>mâlurile</td>
            </tr>
            <tr>
                <th>Dativ-Genitiv</th>
                <td>mâl</td>
                <td>mâlului</td>
                <td>mâluri</td>
                <td>mâlurilor</td>
            </tr>
        </table>
    </div>
[...]
"""

class Gender(Enum):
    Male = "Masculine"
    Female = "Feminine"
    Neuter = "Neuter"

    def __str__(self):
        return self.value

    def parse(s : str):
        return {
            "m" : Gender.Male,
            "f" : Gender.Female,
            "n" : Gender.Neuter
        }[s.lower()[0]]

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.genders = []
        self.tables = []
        self.met_title = False
        self.met_table = False
        self.met_td = False
        self.crt_contents = None


    #HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        #self.lsStartTags.append(startTag)
        if startTag == "div" and ('class', 'cont-list-title') in attrs:
            self.met_title = True
        if startTag == "table" and ('class', 'table-declinare') in attrs:
            self.met_title = False
            self.met_table = True
            self.crt_contents = []
        if startTag == "td":
            self.met_td = True

    def handle_data(self, data):
        if self.met_title:
            for gender in ["masculin", "feminin", "neutru"]:
                if gender in data:
                    self.genders.append(gender)
            self.met_title = False

        if self.met_table:
            if self.met_td:
                self.crt_contents.append(data)
                self.met_td = False

    def handle_endtag(self, endTag):
        if endTag == "table":
            self.met_title = False
            self.met_table = False
            self.met_td = False
            self.tables.append(self.crt_contents)
            self.crt_contents = None

def search_word(word : str) -> dict:
    r = requests.get(f"https://www.pluralul.ro/plural-pentru-{word}.html")
    parser = MyHTMLParser()
    parser.feed(r.text)

    res = []
    for gender, table in zip(parser.genders, parser.tables):
        dic = {
            "word" : table[0],
            "gender" : Gender.parse(gender),
            "Sgl": {
                "Nat": {
                    "Nom": table[0], "Dat": table[4]
                },
                "Art": {
                    "Nom": table[1], "Dat": table[5]
                }
            },
            "Plu": {
                "Nat": {
                    "Nom": table[2], "Dat": table[6]
                },
                "Art": {
                    "Nom": table[3], "Dat": table[7]
                }
            }
        }

        res.append(dic)

    return res

def best_effort(word : str, gender : str) -> dict:
    dic = {
        "word" : word,
        "gender" : Gender.parse(gender)
    }

    g = collapse_gender(gender, "Sgl")
    dic["Sgl"] = {
        "Nat": {
            "Nom": word         , "Dat": word
        },
        "Art": {
            "Nom": word + "-ul" , "Dat": word + "-ului"
        }
    }
    if g == "Feminine":
        dic["Sgl"]["Art"] = {"Nom" : word + "-ei", "Dat": word + "-elei"}

    g = collapse_gender(gender, "Plu")
    dic["Plu"] = {
        "Nat": {
            "Nom": word         , "Dat": word
        },
        "Art": {
            "Nom": word + "-ii" , "Dat": word + "-ilor"
        }
    }
    if g == "Feminine":
        dic["Plu"]["Art"] = {"Nom": word + "-ile", "Dat": word + "-elor"}

    return dic

def collapse_gender(gender: Gender, plural: str) -> Gender:
    """
        Romanian has three genders: Masculine, Feminine and Neuter. If we regard only the singular or plural form,
        then there are only two, since Neuter is a combination of Masculine and Feminine.

        Bascially, convert Neuter to Masculine or Feminine given whether we use the plural or not.
    """
    if type(gender) == str:
        gender = Gender.parse(gender)
    assert type(gender) == Gender
    if gender is Gender.Male or (gender is Gender.Neuter and plural == "Sgl"):
        return Gender.Male
    else:
        return Gender.Female

def compute_path(basefile: Path, tag: str) -> Path:
    return basefile.parent / (basefile.stem) / (tag + basefile.suffix)

def compute_tag(gender: Gender, plural: str, articulated: str, case: str, short=False) -> str:
    assert gender is not Gender.Neuter, "collapse the gender first"
    if not short:
        return f"{str(gender)}_{plural}{articulated}{case}"
    else:
        short_tag = "{0}{1}{2}".format(
            "" if a == "Sgl" else "Plu",
            "" if b == "Nat" else "Art",
            "" if c == "Nom" else "Dat"
        )
        return f"{str(gender)}_{short_tag}" if short_tag != "" else str(gender)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("generate paradigms of words within a textfile. A paradigm is a collection of all possible inflections")
    parser.add_argument("path", type=Path,
                        help="Path towards the file to be declinat..ed?")
    args = parser.parse_args()

    assert args.path.exists()

    basename_alias = ""
    while basename_alias == "":
        basename_alias = input(f"What's the singular form of {args.path.stem}? :")
    (args.path.parent / args.path.stem).mkdir(exist_ok=True)

    files = {}
    backlog = []
    backlog_besteffort = []
    for line in open(args.path, "r", encoding="utf-8-sig").readlines():
        word = line.strip()
        if word == "" or word.startswith("//"):
            continue
        print(f"{word:<20}", end="")

        if len(word.split(" ")) > 1:
            backlog.append(word)
            print("SKIP")
            continue

        results = search_word(word)
        if len(results) > 1:
            print("Multiple found! " + f"https://www.pluralul.ro/plural-pentru-{word}.html"
                    .replace("ă", "a").replace("â", "a").replace("î", "i").replace("ț", "t").replace("ș", "s"))
            for i, res in enumerate(results):
                print(f"{i+1}) {res['word']}")
            while True:
                sel = input("Which one to keep?: ")
                try:
                    sel = int(sel) - 1
                except:
                    continue
                if sel not in range(0, len(results)):
                    continue
                break

            res = results[sel]
        elif len(results) == 1:
            res = results[0]
        else:
            print("NOT FOUND")
            backlog_besteffort.append(word)
            continue
        print("OK")

        for (a, b, c) in itertools.product(["Sgl", "Plu"], ["Nat", "Art"], ["Nom", "Dat"]):
            g = collapse_gender(res["gender"], a)
            tag = compute_tag(g, a, b, c)
            if tag not in files:
                p = compute_path(args.path, tag)
                files[tag] = open(p, "w", encoding="utf-8")
                files[tag].write(f"// These words had their declensed form automatically generated\n\n")

            val = res[a][b][c]
            if val.strip() != "—":
                files[tag].write(f"{val}\n")

    # Declense automatically some words, even if they sound a little weird
    for _, v in files.items():
        v.write(f"\n// These words were declensed in a best-effort manner\n\n")
    for word in backlog_besteffort:
        print(f"{word:<20}Best Effort")
        gender = "?"
        while gender not in ["m", "f", "n"]:
            gender = input(f"What's the gender of '{word}' (m/f/n) ? ").strip()
        res = best_effort(word, gender)

        for (a, b, c) in itertools.product(["Sgl", "Plu"], ["Nat", "Art"], ["Nom", "Dat"]):
            g = collapse_gender(gender, a)
            tag = compute_tag(g, a, b, c)
            if tag not in files:
                p = compute_path(args.path, tag)
                files[tag] = open(p, "w", encoding="utf-8")
                files[tag].write(f"\n// These words were declensed in a best-effort manner\n\n")

            val = res[a][b][c]
            if val.strip() != "—":
                files[tag].write(f"{val}\n")

    # write all items in the backlog as they are
    for _, v in files.items():
        v.write(f"\n// These words couldn't be declensed automatically. Edit manually\n\n")
    for word in backlog:
        gender = "?"
        while gender not in ["m", "f", "n"]:
            gender = input(f"What's the gender of '{word}' (m/f/n) ? ").strip()

        for (a, b, c) in itertools.product(["Sgl", "Plu"], ["Nat", "Art"], ["Nom", "Dat"]):
            g = collapse_gender(gender, a)
            tag = compute_tag(g, a, b, c)
            if tag not in files:
                p = compute_path(args.path, tag)
                files[tag] = open(p, "w", encoding="utf-8")
                files[tag].write(f"\n// These words couldn't be declensed automatically. Edit manually\n\n")

            files[tag].write(f"{word}\n")

    # print out include statements for RulePacks_Global.xml
    basename = args.path.stem
    ref = args.path
    while ref and ref.name != "Strings":
        ref = ref.parent

    print("\n\nDelete the following line from <GlobalUtility.rulePack.rulesFiles>:\n")
    print(f"<li>{basename}->{ref}...</li>")

    print("\n\nAdd these include statements for <GlobalUtility.rulePack.rulesFiles>:\n")
    print(f"<!-- Paradigm of the file {basename}.xml -->")
    aliases = []
    for (g, a, b, c) in itertools.product(["m", "f"], ["Sgl", "Plu"], ["Nat", "Art"], ["Nom", "Dat"]):
        g = collapse_gender(g, a)
        tag = compute_tag(g, a, b, c)
        if tag not in files:
            continue

        short_tag = compute_tag(g, a, b, c, short=True)
        alias = basename_alias + short_tag
        aliases.append(alias)

        path = compute_path(args.path, tag)
        path = path.parent / path.stem
        path = path.relative_to(ref)
        print("    <li>{0}->{1}</li>".format(alias, str(path).replace('\\', '/')))

    print("\n\nAdd these rules for <GlobalUtility.rulePack.rulesStrings>:\n")
    print(f"<!-- Paradigm of the file {basename}.xml -->")
    while aliases:
        alias = aliases[0]
        female_form = alias.replace("Masculine", "Feminine")
        male_form = alias.replace("Feminine", "Masculine")
        genderless_form = alias.replace("Masculine", "").replace("Feminine", "")
        if female_form in aliases:
            print("    <li>{0}->[{1}]</li>".format(genderless_form, female_form))
        if male_form in aliases:
            print("    <li>{0}->[{1}]</li>".format(genderless_form, male_form))

        if female_form in aliases:
            aliases.remove(female_form)
        if male_form in aliases:
            aliases.remove(male_form)