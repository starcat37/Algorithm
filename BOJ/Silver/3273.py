# 3783

import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().split(" "))))
x = int(input())

cnt = 0

for i in nums:
    target = x - i
    if target in nums: cnt += 1
    
print(cnt // 2)