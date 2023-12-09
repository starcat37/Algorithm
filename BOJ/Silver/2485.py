# 2485

from math import gcd
from functools import reduce

def find_gcd(numbers):
  return reduce(gcd, numbers)

trees = []
N = int(input())
for _ in range(N):
  trees.append(int(input()))

intervals = [j-i for i, j in zip(trees, trees[1:])]
final_gcd = find_gcd(intervals)
result = []

for interval in intervals:
  result.append(interval // final_gcd - 1)
  
print(sum(result))
