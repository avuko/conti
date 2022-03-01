#!/usr/bin/env python3
import json
import sys
from deep_translator import GoogleTranslator
import sys
chatList = []
if len(sys.argv) > 2:
    sourcefile = sys.argv[1]
    destfile = sys.argv[2]
else:
    print("This script requires a source and destination file as arguments")
    exit(1)

with open(sourcefile) as f:
    for jsonObj in f:
        _Dict = json.loads(jsonObj)
        chatList.append(_Dict)
with open(destfile, "a") as file_object:
    for line in chatList:
        try:
            translation = GoogleTranslator(source='auto', target='en').translate(line["body"])
            line["LANG-EN"] = translation
        except Exception as e:
            line["LANG-EN"] = "Error during Translation: " + line["body"]
        file_object.write(json.dumps(line, ensure_ascii = False).encode('utf8').decode() + "\n")
