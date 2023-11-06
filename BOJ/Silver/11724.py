# 11724

import sys
input = sys.stdin.readline
from collections import deque

import sys
sys.setrecursionlimit(10000) # 재귀 깊이 제한을 늘림


# 입력 받고 그래프 만들기
N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a) # 양방향 그래프이므로 두 번 append

check = deque([False for i in range(N+1)]) # 방문 목록 - 처음에는 False로 초기화
result = 0 # 연결 요소의 개수

# DFS
def DFS(v):
  check[v] = True # 방문 표시
  for i in range(len(graph[v])):
    next = graph[v][i] # 연결된 다음 정점 선택
    if check[next] == False: # 방문하지 않았을 경우
      DFS(next) # DFS 시행
  
for i in range(1, N+1):
  if check[i] == False: # 방문하지 않은 정점 있을 경우
    DFS(i) # 거기서부터 DFS 시행
    result += 1 # 새로운 하나의 DFS 시작이므로 연결 요소 개수 증가
  
print(result)
