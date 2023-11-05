# 20529

import sys
from itertools import combinations

T = int(input())
for _ in range(T):
  N = int(input())
  *people, = map(str, sys.stdin.readline().strip().split(" "))
  combi = list(combinations(people, 3))
  distance = 0
  for comb in combi:
    distance = count_distance(comb)

def count_distance(comb):