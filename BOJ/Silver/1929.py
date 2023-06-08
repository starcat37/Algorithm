#1929

import math

#소수 판별 함수 정의
def Is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

#입력 받기
M, N = map(int, input().split(' '))
primes = []

#소수일 경우 primes에 추가
for i in range(M, N+1):
    if Is_prime(i) and i!=1:
        primes.append(i)

#결과 출력하기
for n in primes: print(n)