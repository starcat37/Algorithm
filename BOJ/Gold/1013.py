# 1013

import re

T = int(input())
for _ in range(T):
    contact = input()
    print("YES") if re.fullmatch(r"(100+1+|01)+", contact) else print("NO")