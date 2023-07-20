# 10844**

# 메모이제이션 사용한 dp... 어렵다...

N = int(input())
dp = [[0] * 10 for i in range(N)] 
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def isStair(i, j):
    if i == 0: # i == 0: 이미 존재
        return dp[0][j] 
    if dp[i][j] != 0: # 이미 계산한 값
        return dp[i][j]
    if 1 <= j <= 8: # 1~8: ex)3 -> 23 -> 123 <- 12 <- 1
        dp[i][j] = isStair(i-1, j-1) + isStair(i-1, j+1)
        return dp[i][j]
    if j == 0: #0: ex) 1 -> 10
        dp[i][j] = isStair(i-1, 1)
        return dp[i][j]
    if j == 9: #9: ex 9 -> 89 
        dp[i][j] = isStair(i-1, 8)
        return dp[i][j]
    
cnt = 0
for i in range(10):
    cnt += isStair(N-1, i) #N자리 수의 i번째 수

print(cnt % 1000000000)


# def isStair(num):
#     num = list(map(int, list(str(num))))
#     for i in range(len(num)-1):
#         if num[i] - num[i+1] == 1 or num[i] - num[i+1] == -1: 
#             continue
#         else:
#             return 0
#     return 1

# if N == 1:
#     for i in range(1, 10):
#         cnt += isStair(i)
# else:
#     for i in range(10**(N-1), 10**N):
#         cnt += isStair(i)
     
# print(cnt % 1000000000)