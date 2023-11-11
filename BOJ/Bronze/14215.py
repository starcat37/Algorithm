# 14215

lines = list(map(int, input().split()))
lines.sort()

if lines[2] < sum(lines[:2]):
  print(sum(lines))
else:
  print(sum(lines[:2]) * 2 - 1)
