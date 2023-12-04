# 11328

from collections import Counter

N = int(input())
for _ in range(N):
  pattern, target = input().split()
  print("Possible") if Counter(pattern) == Counter(target) else print("Impossible")
