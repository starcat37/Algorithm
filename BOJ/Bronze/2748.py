# 2748

N = int(input())

fibos = [0] * (N+1)

def Fibo(i):
  if i == 1 or i == 2:
    return 1
  if fibos[i]:
    return fibos[i]
  else:
    fibos[i] = Fibo(i-1) + Fibo(i-2)
    return fibos[i]

print(Fibo(N))