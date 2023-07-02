# 2581

import math

def isPrime(x):
    # 2에서 x의 제곱근까지 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False # 소수가 아님
    return True #소수임

M = int(input())
N = int(input())

primes = []

for i in range(M, N+1):
    if i == 1: continue
    else:
        if isPrime(i): 
            primes.append(i)

if primes: 
    print(sum(primes))
    print(min(primes))
else: print(-1)