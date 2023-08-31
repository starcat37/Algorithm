# 1463** 

N = int(input())

dp = [0] * (N+1) # 횟수 메모이제이션, dp[1] = 3 : 1번 인덱스의 수(2)의 연산 횟수가 1이다

for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1 # 1 빼기
    if i % 3 == 0: # 3으로 나누기
        dp[i] = min(dp[i], dp[i//3] + 1) # 
    if i % 2 == 0: # 2로 나누기
        dp[i] = min(dp[i], dp[i//2] + 1)
        
print(dp[N])

# 메모이제이션, dp, 상향식
# DP는 언제쯤 혼자서 풀 수 있을까ㅠㅠ