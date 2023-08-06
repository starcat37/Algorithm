# 11723

import sys

S = set()

M = int(input())
for _ in range(M):
    calc = sys.stdin.readline().rstrip().split()
    command = calc[0]
    if command == "add":
        x = int(calc[1])
        if x not in S: S.add(x)
    elif command == "remove":
        x = int(calc[1])
        if x in S: S.remove(x)
    elif command == "check":
        x = int(calc[1])
        if x in S: print(1)
        else: print(0)
    elif command == "toggle":
        x = int(calc[1])
        if x in S: S.remove(x)
        else: S.add(x)
    elif command == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif command == "empty":
        S = set()