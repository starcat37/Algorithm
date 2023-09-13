# 2294

n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))
  
coins.sort()
dp = [float("inf")] * (k+1) # 양의 무한대 표시
dp[0] = 0 # '번째'로 세기 위해 0은 0으로 미리 할당

for coin in coins: # 1종류 사용 -> 2종류 사용 -> ...
  for i in range(coin, k+1): # coin 값부터 k값까지
    dp[i] = min(dp[i-coin] + 1, dp[i]) # i 값에서 동전 값을 뺐을 때 값 vs dp[i] 자체의 값(이전 동전들까지만 사용했을 때 개수)

if dp[-1] == float('inf'):
  print(-1) # k번째까지 돌았을 때 해당 동전들로 값을 만들 수 없으면 inf로 유지됨
else:
  print(dp[-1])