# 1735

D_1, N_1 = map(int, input().split())
D_2, N_2 = map(int, input().split())

D_3 = D_1 * N_2 + D_2 * N_1
N_3 = N_1 * N_2

# 최대공약수
def GCD(x, y):
  while(y):
    x, y = y, x%y
  return x

gcd = GCD(D_3, N_3)
print(D_3//gcd, N_3//gcd)
