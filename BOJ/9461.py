# 9461

waves = [0, 1, 1, 1] + [-1 for i in range(97)]
def getWave(N):
  if N <= 3:
    return 1
  if waves[N] != -1:
    return waves[N]
  else:
    waves[N] = getWave(N-2) + getWave(N-3)
    return waves[N]

T = int(input())
for _ in range(T):
  N = int(input())
  answer = getWave(N)
  print(answer)