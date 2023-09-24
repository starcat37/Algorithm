# 16964**

import sys
input = sys.stdin.readline

N = int(input())
graph = {i:[] for i in range(1, N+1)}
visited = [False for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

order = list(map(int, input().rstrip().split()))
order_dict = {node: idx for idx, node in enumerate(order)}

for node in graph.keys():
  graph[node].sort(key=lambda x: order_dict[x])
  
stack = [1]
visited[1] = True
order_idx = 0

while stack:
    current_node = stack.pop()
    
    if current_node != order[order_idx]:
        print(0)
        break
    
    order_idx += 1
    
    for neighbor in reversed(graph[current_node]):
        if not visited[neighbor]:
            stack.append(neighbor)
            visited[neighbor] = True
else:
    print(1)

# result = 1

# for i in range(1, N):
#   if visited[order[i]]:
#     continue
#   else:
#     visited[order[i]] = True
#     if order[i+1] not in graph[order[i]]:
#       result = 0
#       # print(graph[order[i]], result)
#       break
#     else:
#       continue
    
# print(result)