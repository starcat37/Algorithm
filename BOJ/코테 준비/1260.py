# 1260
# DFS와 BFS

# 입력받고 그래프 선언
from collections import deque
import sys

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)
  
for i in range(N+1):
  graph[i].sort() # 번호가 작은 노드부터 방문하기 위해 정렬

# DFS
def DFS(v):
  print(v, end=" ")
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

visited = [False] * (N+1)
DFS(V)
print()

# BFS 
def BFS(v):
  queue = deque()
  queue.append(v)
  visited[v] = True
  while queue:
    current_node = queue.popleft()
    print(current_node, end=" ")
    for i in graph[current_node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        
visited = [False] * (N+1)
BFS(V)
