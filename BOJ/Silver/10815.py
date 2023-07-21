# 10815

import sys
from collections import Counter

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
nums = list(map(int, sys.stdin.readline().split()))

answer = Counter(cards)
print(" ".join(f"{answer[num]}" if num in answer else '0' for num in nums))