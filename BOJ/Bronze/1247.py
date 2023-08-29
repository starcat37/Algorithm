# 1247

import sys

for _ in range(3):
    N = int(sys.stdin.readline().strip())
    result = 0
    for _ in range(N):
        result += int(sys.stdin.readline().strip())
    if result == 0:
        print("0")
    elif result > 0:
        print("+")
    else:
        print("-")