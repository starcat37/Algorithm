# 2563

paper = []

N = int(input())
for _ in range(N):
  x, y = map(int, input().split())
  paper.append([(x, x+10), (y, y+10)])
  
print(paper)