# 2720

T = int(input())
for _ in range(T):
  C = int(input())
  Q = C // 25
  D = (C-Q*25) // 10
  N = (C-Q*25-D*10) // 5
  P = (C-Q*25-D*10-N*5) // 1
  print(Q, D, N, P)
