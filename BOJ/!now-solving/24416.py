# 24416

N = int(input())

def fib(n):
  if n == 1 or n == 2: return 1
  else: return fib(n-1) + fib(n-2)
  
memo = [0 * 50]  

def fibonacci(n):
  memo[1]