# 11478

S = input()
length = len(S)
parts = set()

for i in range(length):
  for j in range(i, length):
    parts.add(S[i:j+1])
    
print(len(parts))
