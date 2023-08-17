# 2480

*nums, = map(int, input().split(" "))
cnt = []
for i in nums:
    cnt.append(nums.count(i))
    
if max(cnt) == 1:
    print(max(nums) * 100)
elif max(cnt) == 2:
    print(1000 + nums[cnt.index(2)] * 100)
else:
    print(10000 + max(nums) * 1000)