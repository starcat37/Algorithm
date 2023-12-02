# 15904

import re

result = ""

Uppers = "".join(re.findall(r"[A-Z]", input()))
for c in Uppers:
  if c == "U" and result == "":
    result += c
  elif c == "C" and result == "U":
    result += c
  elif c == "P" and result == "UC":
    result += c
  elif c == "C" and result == "UCP":
    result += c
    break

print("I love UCPC") if result == "UCPC" else print("I hate UCPC")
