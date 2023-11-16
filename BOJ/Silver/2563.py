# 2563**
# 이중 리스트를 좌표처럼 사용하자
# 새로운 접근이라 기억해두면 좋을 듯

import sys
input = sys.stdin.readline

paper = [[0] * 101 for i in range(101)]

for _ in range(int(input())):
  a, b = map(int, input().split())
  for i in range(10):
    for j in range(10):
      paper[a+i][b+j] = 1

result = 0
for row in paper:
  result += sum(row)
  
print(result)
