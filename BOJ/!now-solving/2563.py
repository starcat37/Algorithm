# 2563

paper = []

N = int(input())
all_paper = N * 100

for _ in range(N):
  x, y = map(int, input().split())
  paper.append([(x, x+10), (y, y+10)])
  
# (5, 7), (13, 7), (5, 12), (13, 12)