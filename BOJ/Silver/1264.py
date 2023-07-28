# 1264

import re

while True:
    sentence = input()
    if sentence == "#":
        break
    else:
        print(len(re.findall("[aeiouAEIOU]", sentence)))