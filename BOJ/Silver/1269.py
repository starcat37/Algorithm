# 1269

import sys
input = sys.stdin.readline

numA, numB = map(int, input().rstrip().split())
set_A = set(map(int, input().rstrip().split()))
set_B = set(map(int, input().rstrip().split()))

print(len(set_A ^ set_B))
