# 5648**

import sys

nums = "".join(list(map(str, sys.stdin.readlines()))).split() # 입력 문제: re.split은 구분자 사이에 아무것도 없을 경우 빈 문자열이 들어감..
reverses = []

for i in range(1, int(nums[0])+1):
    reverses.append(int(nums[i][::-1])) #문자열 뒤집기: str[::-1]
  
for j in sorted(reverses):
    print(j)

# cnt, *nums = sys.stdin.read().split()
# for i in range(int(cnt)):
#     nums[i] = nums[i][::-1]
# nums = list(map(int, nums))
# print(*sorted(nums), sep="\n")
