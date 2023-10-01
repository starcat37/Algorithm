# 1654

import sys
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
lines = []

for _ in range(K):
  lines.append(int(input()))
  
print(lines)