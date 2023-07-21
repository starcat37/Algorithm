# 18110

import sys

opnions = []

n = int(input())
if n:
    cut = round(n * 0.15 + 0.0000001)
    for _ in range(n):
       opnions.append(int(sys.stdin.readline()))
    opnions.sort()
    if cut: print(round(sum(opnions[cut:-cut]) / (n-cut*2) + 0.0000001))
    else: print(round(sum(opnions) / (n-cut*2) + 0.0000001))

else:
    print(0)