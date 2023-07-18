#10816**

import sys
from collections import Counter

#입력 받기
N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
nums = list(map(int, sys.stdin.readline().split()))

#Counter 사용
answer = Counter(cards)
print(" ".join(f'{answer[num]}' if num in answer else '0' for num in nums))

# Counter는 딕셔너리 접근 -> O(1)
# N번 접근하면 O(N)