#2108

import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()

def max_count(nums):
    c_list = Counter(nums).most_common()
    maximum = c_list[0][1]

    modes = []
    for n in c_list:
        if n[1] == maximum:
            modes.append(n[0])
    if len(modes) != 1:
        return sorted(modes)[1]
    else:
        return sorted(modes)[0]


print(round(sum(nums)/len(nums)))
print(nums[len(nums) // 2])
print(max_count(nums))
print(nums[-1] - nums[0])