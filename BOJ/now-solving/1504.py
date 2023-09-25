# 1504

import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().rstrip().split())
graph = {i:[] for i in range(1, N+1)}
dist = 0

for _ in range(E):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
  
v1, v2 = map(int, input().rstrip().split())

def dijkstra(graph, start):
  distances = {node: float("inf") for node in graph}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, (distances[start], start))
  
  while queue:
    cur_dist, cur_dest = heapq.heappop(queue)
    
    if distances[cur_dest] < cur_dist:
      continue
    
    for next_dest, next_dist in graph[cur_dest]:
      distance = cur_dist + next_dist
      if distance < distances[next_dest]:
        distances[next_dest] = distance
        heapq.heappush(queue, (distance, next_dest))
  
  return distances
  
dist_1 = dijkstra(graph, 1)
dist_v1 = dijkstra(graph, v1)
dist_v2 = dijkstra(graph, v2)

path1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
result = min(path1, path2)

print(result if result != float("inf") else -1)
