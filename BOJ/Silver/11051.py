# 11051

import sys
sys.setrecursionlimit(10**6)

def factorial(N):
    if N > 1:
        return N * factorial(N-1)
    else:
        return 1

N, K = map(int, input().split(" "))

print(factorial(N)//(factorial(K)*factorial(N-K)) % 10007)
