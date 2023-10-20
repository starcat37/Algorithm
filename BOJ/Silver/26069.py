# 26069

import sys
input = sys.stdin.readline

rainbow_dance = {"ChongChong", }

N = int(input())
for _ in range(N):
  name_A, name_B = map(str, input().rstrip().split())
  if name_A in rainbow_dance or name_B in rainbow_dance:
    rainbow_dance.update([name_A, name_B])
    
print(len(list(rainbow_dance)))
