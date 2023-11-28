# 1225

A, B = map(str, input().split())
result = 0

for a in A:
  for b in B:
    result += int(a) * int(b)
    
print(result)
