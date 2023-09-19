# 27433

N = int(input())
def factorial(N):
  if N == 0:
    return 1
  else:
    return N * factorial(N-1)
   
result = factorial(N) 
print(result)