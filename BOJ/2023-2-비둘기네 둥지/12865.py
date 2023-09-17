# 12865

import sys

N, K = map(int, sys.stdin.readline().strip().split())
objects = [(0, 0)]
for _ in range(N):
  W, V = map(int, sys.stdin.readline().strip().split())
  objects.append((W, V))
  
objects.sort()
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(K+1):
  for j in range(N+1):
    dp[i][j] = dp[i][j-1]
    if objects[j][0] <= i:
      dp[i][j] = max(dp[i][j], dp[i-objects[j][0]][j-1] + objects[j][1])
      
print(dp[-1][-1])