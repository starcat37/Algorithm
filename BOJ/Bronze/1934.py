# 1934
# 유클리드 호제법

# 최대공약수
def GCD(x, y):
  while(y):
    x, y = y, x%y
  return x

# 최소공배수
def LCM(x, y):
  return (x*y) // GCD(x, y)

T = int(input())
for _ in range(T):
  x, y = map(int, input().split())
  print(LCM(x, y))
