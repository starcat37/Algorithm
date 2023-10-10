# 9996

import re

N = int(input())
raw_pattern = input()
pattern = re.sub(r"[*]", "[a-z]*", raw_pattern)

for _ in range(N):
  string = input()
  if re.fullmatch(pattern, string):
    print("DA")
  else:
    print("NE")