# 1298

from collections import deque

# bfs + 분배
def solution(graph):
  pass


# 입력 받기
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = {i:[] for i in range(1, N+1)}
while True:
  try:
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
  except:
    break
  
print(graph)

# start와 end point로 묶어주기
graph
