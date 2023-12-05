# 4948

import math

def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

while True:
  prime_cnt = 0
  n = int(input())
  if n == 0: break
  for num in range(n+1, 2*n+1):
    if is_prime(num) and num != 1:
      prime_cnt += 1 
  print(prime_cnt)
