# 10867

import sys

N = int(input())
nums = " ".join(map(str, sorted(list(set(list(map(int, sys.stdin.readline().split(" "))))))))
print(nums)