# 2775
# 0-1: 1, 0-2: 2, 0-3: 3
# 1-1: 1, 1-2: 1+2, 1-3: 1+2+3
# 2-1: 1, 2-2: 1+1+2, 2-3: 1+1+2+1+2+3

memo = [[0] * 15 for _ in range(15)]

def dp(k, n):
    if k == 0:
        memo[k][n] = n
        return n
    else:
        if memo[k][n] != 0:
            return memo[k][n]
        else:
            total = 0
            for i in range(1, n+1):
                total += dp(k-1, i)
            memo[k][n] = total
            return total


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp(k, n))