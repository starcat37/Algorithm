# 25191

N = int(input())
A, B = map(int, input().split())

available_home = A // 2 + B
if available_home > N:
  print(N)
else:
  print(available_home)
