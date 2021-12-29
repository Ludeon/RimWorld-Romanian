#!/bin/python3.9
from pathlib import Path
from collections import defaultdict
from enum import Enum
import argparse
import csv

PATH=Path("Core/Strings/Words/Nouns.csv")
COLS=["Filename","original","gender","SglNom","SglArt","SglDat","SglVoc","PluNom","PluArt","PluDat","PluVoc"]
ECOLS=COLS[3:]

# Mapping from filename to include-rule-name, as it's not consistent... Some rules are even implicit
MAPPINGS={
    "AnimalGroups"              : "AnimalGroup",
    "Animals"                   : "Animal",
    "Animals_Badass"            : "AnimalBadass",
    "Apparel"                   : "Apparel",
    "Artworks"                  : "Artwork",        # !!! originally not in RulePacks_Global.xml
    "Bodyparts"                 : "BodyPart",
    "BusinessTypes"             : "businesstype",   # !!! originally not in RulePacks_Global.xml
    "Colors"                    : "Color",
    "Colors_Badass"             : "ColorBadass",
    "Communities"               : "Community",
    "Concepts_Angsty"           : "ConceptAngsty",
    "Concepts_Badass"           : "ConceptBadass",
    "Concepts_Positive"         : "ConceptPositive",
    "Enemies"                   : "Enemy",
    "Games"                     : "Game",
    "Gore"                      : "Gore",
    "GroupNames"                : "groupname",      # !!! originally not in RulePacks_Global.xml
    "Mechanoid"                 : "Mechanoid",
    "NaturalObject"             : "NaturalObject",
    "People_Allies"             : "PersonAlly",
    "People_Badass"             : "PersonBadass",
    "People_Family"             : "PersonFamily",
    "People_Jobs"               : "PersonJob",
    "PersonalCharacteristics"   : "PersonalCharacteristic",
    "PoliticalUnions_Outlander" : "political_union_outlander", # !!! originally not in RulePacks_Global.xml
    "PoliticalUnions_Tribal"    : "political_union_tribal", # !!! originally not in RulePacks_Global.xml
    "Quests"                    : "quest",                  # !!! originally not in RulePacks_Global.xml
    "Stories"                   : "story",                  # !!! originally not in RulePacks_Global.xml
    "TalkTopics_Heavy"          : "talktopicheavyfile", # !!! originally not in RulePacks_Global.xml
    "TalkTopics_Light"          : "talktopiclightfile", # !!! originally not in RulePacks_Global.xml
    "TerrainFeatures"           : "TerrainFeature",
    "TreeTypes"                 : "TreeType",
    "Vegetables"                : "Vegetable",
    "Weapons"                   : "Weapon",
}

class Gender(Enum):
    Male = "Msc"
    Female = "Fem"
    Neuter = "Neu"

    def __str__(self):
        return self.value

    def parse(s : str):
        return {
            "m" : Gender.Male,
            "f" : Gender.Female,
            "n" : Gender.Neuter
        }[s.lower()[0]]

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
        defaultPath.parent.mkdir(parents=True, exist_ok=True)
        with open(defaultPath, "w", encoding="utf-8") as f:
            items = list(filter(lambda x: x, map(lambda x: x["original"], lines)))
            f.write(f"// NOTE: This file was auto-generated with data from {PATH}\n")
            f.write("\n".join(items))

        for col in ECOLS:
            for gender in [Gender.Male, Gender.Female]:
                items = []
                for x in lines:
                    if not x["gender"] or not x["SglNom"]:
                        continue
                    crt_gender_collapsed = collapse_gender(Gender.parse(x["gender"]), col.startswith("Plu"))
                    if gender == crt_gender_collapsed and x[col] and x[col] != "-":
                        items += [x[col]]
                if len(items) == 0:
                    continue

                crtPath = basePath / filename / f"{gender}{col}.txt"
                incRules += [f"<li>{MAPPINGS[filename]}_{gender}{col}->Words/Nouns/{filename}/{gender}{col}</li>"]
                anyGenderRules += [f"<li>{MAPPINGS[filename]}_{col}->[{MAPPINGS[filename]}_{gender}{col}]</li>"]

                crtPath.parent.mkdir(parents=True, exist_ok=True)
                with open(crtPath, "w", encoding="utf-8") as f:
                    f.write(f"// NOTE: This file was auto-generated with data from {PATH}\n")
                    f.write("\n".join(items))

    print("for <GlobalUtility.rulePack.rulesFiles>:\n")
    print("    <!-- START OF Nouns -->")
    print("\n".join(map(lambda x: " "*4 + x, incRules)))
    print("    <!-- END OF Nouns -->\n")

    print("for <GlobalUtility.rulePack.rulesStrings>\n")
    print("    <!-- START OF Nouns; if gender is not specified, use any -->")
    print("\n".join(map(lambda x: " "*4 + x, anyGenderRules)))
    print("    <!-- END OF Nouns -->\n")