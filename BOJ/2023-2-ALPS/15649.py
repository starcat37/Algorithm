# 15649

# 1. itertools 사용
from itertools import permutations
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]

for i in list(permutations(nums, M)):
  print(" ".join(map(str, i)))

# 2. 직접 순열 구현 - 재귀 사용
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]

def my_perm(nums: list[int], r: int):
  result = []
  if r == 0:
    return [tuple()]
  for i in range(len(nums)):
    item = nums[i]
    for other in my_perm(nums[:i] + nums[i+1:], r-1):
      result.append((item,) + other)
  return result
  
for i in list(my_perm(nums, M)):
  print(" ".join(map(str, i)))
