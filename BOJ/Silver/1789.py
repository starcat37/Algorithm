# 1789

S = int(input())

for i in range(1, S+1):
  if S - i < 0:
    break
  S -= i
  N = i

print(N)

# 당연히 시간 초과
# S = int(input())
# num = 0
# N = 0
# i = 1

# while True:
#   if num == S: break
#   else:
#     num += i
#     i += 1
#     N += 1

# print(N)


