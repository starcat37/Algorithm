# 1026

result = 0

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B)

for i in range(N):
  result += A[i] * B[i]
  
print(result)
