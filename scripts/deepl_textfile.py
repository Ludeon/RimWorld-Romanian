import sys
import requests
import os
from pathlib import Path
from typing import List

deepl_key = os.getenv("DEEPL_KEY")
if deepl_key is None:
    print("missing deepl key. plase set 'DEEPL_KEY' environment variable")
    exit(0)

if len(sys.argv) != 2:
    print("wrong invokation.\nusage:./script.py <file>")
    exit(0)
path = Path(sys.argv[1])

def deepl_translate(lines : List[str]) -> str:
    r = requests.post(
                url="https://api-free.deepl.com/v2/translate",
                data={
                    "target_lang": "RO",
                    "auth_key": deepl_key,
                    "text": lines,
                },
            )
    tlines = list(map(lambda x : x["text"], r.json()["translations"]))
    assert len(tlines) == len(lines)
    return tlines

with open(str(path), "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = map(lambda x : x.strip(), lines)
lines = list(filter(lambda x : len(x) > 0, lines))
print(f"There are {len(lines)} lines")
n_chars = len("".join(lines))

lines = deepl_translate(lines)

with open(str(path.stem) + "_translated" + str(path.suffix), "w", encoding="utf-8") as f:
    f.write("\n\n".join(lines))

print(f"Finished translation. Translated {n_chars} characters")