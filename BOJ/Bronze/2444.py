# 2444

N = int(input())

for i in range(1, N):
    result = " " * (N-i) + "*" * i  + "*" * (i-1)
    print(result)
    
for i in range(N, 0, -1):
    result = " " * (N-i) + "*" * i + "*" * (i-1)
    print(result)