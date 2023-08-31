# 2747

N = int(input())

fibos = [0] * (N+1)

for i in range(1, N+1):
  if i == 1 or i == 2:
    fibos[i] = 1
  else: 
    fibos[i] = fibos[i - 1] + fibos[i - 2]
    
print(fibos[N])