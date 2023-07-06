# 15688 - nlogn sorting X

import sys

N = int(input())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))
    
for j in sorted(nums):
    print(j)