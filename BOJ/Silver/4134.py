# 4134

import math

def Is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

T = int(input())
for _ in range(T):
  n = int(input())
  for num in range(n, 4*10**9+8):
    if Is_prime(num):
      if n == 0 or n == 1 or n == 2:
        print(2)
        break
      print(num)
      break
