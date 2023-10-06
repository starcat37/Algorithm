# 10820

import re

while True:
  try:
    string = input()
    print(len(re.findall(r"[a-z]", string)), len(re.findall(r"[A-Z]", string)), len(re.findall(r"[0-9]", string)), len(re.findall(r" ", string)))
  except:
    break
