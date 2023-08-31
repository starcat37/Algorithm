# 10870

N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
  if i == 1 or i == 2:
    dp[i] = 1
  else:
    dp[i] = dp[i - 1] + dp[i - 2]
    
print(dp[N])