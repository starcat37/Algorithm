# 12789

N = int(input())
line = list(map(int, input().split()))
stack = []
current = 1

while line:
  if line[0] == current:
    line.pop(0)
    current += 1
  else:
    stack.append(line.pop(0))
    
  while stack:
    if stack[-1] == current:
      stack.pop()
      current += 1
    else:
      break

print("Nice" if not stack else "Sad")
