# 2355

A, B = map(int, input().split(" "))
result = 0

if A > B:
    A, B = B, A
    
print(int((B - A + 1) * (A + B) / 2))