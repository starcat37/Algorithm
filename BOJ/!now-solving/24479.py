# 24479

# DFS 선언
def DFS(graph, start):
  visited[start] = True
  print(start)
  for v in graph[start]:
    if not visited[v]: DFS(graph, v)

# 입력 받고 그래프 만들기
N, M, R = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)

for v in graph:
  graph[v].sort()

visited = [False] * (N+1)
DFS(graph, 1)
