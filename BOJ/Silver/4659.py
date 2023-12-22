# 4659

import re

def check(string):
  if not re.findall(r"[aeiou]", string):
    return False
  if re.search(r"[aeiou]{3}", string):
    return False
  if re.search(r"[^aeiou]{3}", string):
    return False
  if re.search(r"(?!ee|oo)(.)\1", string):
    return False
  return True

while True: 
  string = input()
  if string == "end": break
  if check(string):
    print(f"<{string}> is acceptable.")
  else:
    print(f"<{string}> is not acceptable.")
