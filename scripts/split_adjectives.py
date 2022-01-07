#!/bin/python3.9
from pathlib import Path
from collections import defaultdict
import argparse
import csv

PATH=Path("Core/Strings/Words/Adjectives.csv")
COLS=["Filename","original","MscSgl","MscPlu","FemSgl","FemPlu"]
ECOLS=COLS[2:]

MAPPINGS={
    "Angsty"            : "AdjectiveAngsty",
    "Badass"            : "AdjectiveBadass",
    "Colors"            : "AdjectiveColor",       # !!! extra for Romanian
    "Colors_Badass"     : "AdjectiveColorBadass", # !!! extra for Romanian
    "CompassDirections" : "AdjectiveDirection",   # !!! extra for Romanian
    "Curious"           : "adjectiveCurious",     # !!! originally an implicit include
    "Friendly"          : "AdjectiveFriendly",
    "Large"             : "AdjectiveLarge",
    "Natural"           : "AdjectiveNatural",
    "PoliticalUnions"   : "political_adjective",  # !!! originally an implicit include
}

def read_data(path: Path):
    groups = defaultdict(list)
    with open(PATH, "r", encoding="utf-8") as f:
        csvFile = csv.DictReader(f)

        for line in csvFile:
            assert all(map(lambda x: x in COLS, line.keys()))
            fn = line["Filename"]
            del line["Filename"]
            groups[fn] += [line]
    return groups

if __name__ == "__main__":
    assert PATH.exists()
    assert PATH.is_file()
    assert PATH.suffix == ".csv"

    basePath = PATH.parent / PATH.stem
    groups = read_data(PATH)
    incRules = []
    anyGenderRules = []

    for filename, lines in groups.items():
        defaultPath = basePath / (filename + ".txt")
        with open(defaultPath, "w", encoding="utf-8") as f:
            items = list(filter(lambda x: x, map(lambda x: x["original"], lines)))
            f.write(f"// NOTE: This file was auto-generated with data from {PATH}\n")
            f.write("\n".join(items))

        for col in ECOLS:
            crtPath = basePath / filename / (col + ".txt")
            incRules += [f"<li>{MAPPINGS[filename]}_{col}->Words/Adjectives/{filename}/{col}</li>"]
            if col.startswith("Msc"):
                anyGenderRules += [f"<li>{MAPPINGS[filename]}_{col[3:]}->{MAPPINGS[filename]}_{col}</li>"]

            crtPath.parent.mkdir(parents=True, exist_ok=True)
            with open(crtPath, "w", encoding="utf-8") as f:
                items = list(filter(lambda x: x, map(lambda x: x[col], lines)))
                f.write(f"// NOTE: This file was auto-generated with data from {PATH}\n")
                f.write("\n".join(items))

    print("for <GlobalUtility.rulePack.rulesFiles>:\n")
    print("    <!-- START OF Adjectives -->")
    print("\n".join(map(lambda x: " "*4 + x, incRules)))
    print("    <!-- END OF Adjectives -->\n")

    print("for <GlobalUtility.rulePack.rulesStrings>\n")
    print("    <!-- START OF Adjectives; if gender is not specified, use masculine -->")
    print("\n".join(map(lambda x: " "*4 + x, anyGenderRules)))
    print("    <!-- END OF Nouns -->\n")