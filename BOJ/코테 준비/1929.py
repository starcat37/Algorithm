# 1929
# 소수 판별

import math

# 소수 판별 알고리즘 - 2부터 제곱근까지 나눠보기
def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0: return False
  return True

M, N = map(int, input().split())
primes = []

for i in range(M, N+1):
  if is_prime(i) and i != 1: # 1은 소수가 아님
    primes.append(i)
    
for number in primes: print(number)
