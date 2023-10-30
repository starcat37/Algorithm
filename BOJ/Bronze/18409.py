# 18409

import re

N = int(input())
S = input()

print(len(re.findall(r"[aeiou]", S)))
