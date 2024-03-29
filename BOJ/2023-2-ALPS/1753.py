# 1753

import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().rstrip().split())
graph = {i:[] for i in range(1, V+1)}
K = int(input())
for _ in range(E):
  u, v, w = map(int, input().rstrip().split())
  graph[u].append((v, w))

# 다익스트라
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

result = dijkstra(graph, K)
for i in result.items():
  if i[1] == float("inf"):
    print("INF")
  else:
    print(i[1])
    
# https://c4u-rdav.tistory.com/50
# https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python