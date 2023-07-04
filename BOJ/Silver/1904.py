# 1904
# 1 2 3 5 8 -> 피보나치 수열..?

N = int(input())

cnt = [0] * (N+1)
if N == 1:
  cnt[1] = 1
else:
  cnt[1] = 1
  cnt[2] = 2


if N >= 3:
  for i in range(3, N+1):
    cnt[i] = (cnt[i-1] + cnt[i-2]) % 15746
  print(cnt[N])
else:
  print(cnt[N])