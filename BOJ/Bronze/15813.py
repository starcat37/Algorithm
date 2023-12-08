# 15813

N = input()
name = list(input())
result = 0

for c in name:
  result += ord(c) - 64
  
print(result)
