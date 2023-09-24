# 1504

import sys
input = sys.stdin.readline

N, E = map(int, input().rstrip().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(E):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
  
v1, v2 = map(int, input().rstrip().split())

print(graph)