#!/bin/python3.9
from html.parser import HTMLParser
from pathlib import Path
import requests
import argparse
import itertools
from enum import Enum
import pyperclip

"""
Example exerpt of response from https://ro.wiktionary.org/wiki/c%C4%83tun:

[...]
<table>
    <tbody>
        <tr>
            <td colspan="3">
                <b>Declinarea substantivului <br><span>cătun</span></b>
            </td>
        </tr>
        <tr>
            <td><i>n.</i></span></b>
            </td>
            <td><b>Singular</b>
            </td>
            <td><b>Plural</b>
            </td>
        </tr>
        <tr>
            <td><b>Nominativ-Acuzativ </b>
            </td>
            <td><b>cătun</b>
            </td>
            <td><b>cătunuri</b>
            </td>
        </tr>
        <tr>
            <td><b>Articulat </b>
            </td>
            <td><b>cătunul</b>
            </td>
            <td><b>cătunurile</b>
            </td>
        </tr>
        <tr>
            <td><b>Genitiv-Dativ </b>
            </td>
            <td><b>cătunului</b>
            </td>
            <td><b>cătunurilor</b>
            </td>
        </tr>
        <tr>
            <td><b>Vocativ </b>
            </td>
            <td><b>cătunule</b>
            </td>
            <td><b>cătunurilor</b>
            </td>
        </tr>
    </tbody>
</table>
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
            "m." : Gender.Male,
            "f." : Gender.Female,
            "n." : Gender.Neuter
        }[s.lower()[0]]

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.met_title = False
        self.met_table = False
        self.crt_contents = None

    #HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        if startTag == "table":
            self.met_table = True
            self.crt_contents = []

    def handle_data(self, data):
        if self.met_table:
            if "Declinarea" in data:
                self.met_title = True
                if "adjectiv" in data:
                    self.met_table = False
        if self.met_table and self.met_title:
            data = data.strip()
            if data != "":
                if data in ["'", "invariabil"]:
                    data = "-"
                self.crt_contents.append(data)

    def handle_endtag(self, endTag):
        if endTag == "table":
            self.met_table = False
            self.met_title = False
            if self.crt_contents:
                self.tables.append(self.crt_contents)
            self.crt_contents = None

def search_word(word : str) -> dict:
    r = requests.get(f"https://ro.wiktionary.org/wiki/{word}")
    parser = MyHTMLParser()
    parser.feed(r.text)

    res = []
    for table in parser.tables:
        if len(table) == 16:
            table = ["asd"] + table
        if len(table) != 17:
            continue
        table = list(map(lambda x: x.split(",")[0], table))
        dic = {
            "gender" : table[2][0],
            "SglNom" : table[6],
            "SglAcc" : table[9],
            "SglDat" : table[12],
            "SglVoc" : table[15],
            "PluNom" : table[7],
            "PluAcc" : table[10],
            "PluDat" : table[13],
            "PluVoc" : table[16],
        }
        res.append(dic)

    return res

if __name__ == "__main__":
    while ((input("Press enter (w data in clipboard), or type exit: ")) != "exit"):
        text = pyperclip.paste()
        words = text.split("\n")
        words = list(map(lambda x: x.strip(), words))
        paradigms = []

        for word in words:
            res = search_word(word)

            if len(res) == 0:
                paradigms.append(["", word])
                continue

            if len(res) > 1:
                print(f"Multiple results found for {word}:\n  ", end="")
                for k in res[0].keys():
                    print(f"|{k:^10}", end="")
                print("")
                for i, dic in enumerate(res):
                    print(f"{i+1}.", end="")
                    for v in dic.values():
                        print(f"|{v:^10}", end="")
                    print("")
                ans = "asd"
                while True:
                    ans = input("\n Which one to keep? ")
                    try:
                        ans = int(ans)
                        if ans < 1 or ans > len(res):
                            continue
                        else:
                            break
                    except:
                        continue
                res[0] = res[ans-1]

            paradigms.append(list(res[0].values()))

        s = ""
        for p in paradigms:
            s += "\t".join(p) + "\n"
        print("Summary:")
        print(s)
        pyperclip.copy(s)
        print("Copied summary to clipboard")