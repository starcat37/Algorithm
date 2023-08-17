# 25304

X = int(input())
N = int(input())
real = 0
for _ in range(N):
    a, b = map(int, input().split(" "))
    real += a * b
    
print("Yes") if X == real else print("No")