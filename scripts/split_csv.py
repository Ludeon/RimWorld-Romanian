#!/bin/python3.9
from pathlib import Path
from collections import defaultdict
import argparse
import csv

def read_data(path: Path):
    groups = defaultdict(list)
    with open(args.path, "r", encoding="utf-8") as f:
        csvFile = csv.DictReader(f)

        for line in csvFile:
            fn = line["Filename"]
            del line["Filename"]
            groups[fn] += [line]
    return groups

if __name__ == "__main__":
    parser = argparse.ArgumentParser("split a csv file into a format that can be loaded by the game")
    parser.add_argument("path", type=Path,
                        help="Path towards the file to be split")
    args = parser.parse_args()

    assert args.path.exists()
    assert args.path.suffix == ".csv"

    basePath = args.path.parent / args.path.stem
    groups = read_data(args.path)
    incRules = []

    for k, v in groups.items():
        defaultPath = basePath / (k + ".txt")

        columns = list(x for x in v[0].keys() if x != "original")
        for col in columns:
            crtPath = basePath / k / (col + ".txt")
            incRules += [f"<li>Adjective{k}{col}->Words/Adjectives/{k}/{col}</li>"]

            crtPath.parent.mkdir(parents=True, exist_ok=True)
            with open(crtPath, "w", encoding="utf-8") as f:
                items = list(filter(lambda x: x, map(lambda x: x[col], v)))
                f.write(f"// NOTE: This file was auto-generated with data from {args.path}\n")
                f.write("\n".join(items))

    print("for <GlobalUtility.rulePack.rulesFiles>:\n")
    print("    <!-- START OF Adjectives -->")
    print("\n".join(map(lambda x: " "*4 + x, incRules)))
    print("    <!-- END OF Adjectives -->")