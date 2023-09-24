# 1766

import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
workbook = {i:[] for i in range(1, N+1)} # 그래프
indegree = [0] * (N+1) # 자기 자신으로 들어오는 간선의 개수 리스트

for _ in range(M):
  A, B = map(int, input().split())
  workbook[A].append(B)
  indegree[B] += 1

# 위상정렬
def topology_sort():
  result = []
  heap = []
  
  # 1. 자기 자신으로 들어오는 간선이 없는 정점 큐에 넣기
  for i in range(1, N+1):
    if indegree[i] == 0:
      heapq.heappush(heap, i)

  # 2. 큐가 빌 때까지 pop한 정점에서 나오는 간선 제거
  while heap:
    work = heapq.heappop(heap)
    result.append(work)

    # 3. 큐에서 꺼낸 정점과 연결된 정점을 탐색
    for next_work in workbook[work]:
      indegree[next_work] -= 1
      # 4. 자기 자신으로 들어오는 간선이 0개일 경우 queue에 넣기
      if indegree[next_work] == 0:
        heapq.heappush(heap, next_work)
  
  return result

result = topology_sort()
print(" ".join(map(str, result)))

# heap queue, 우선순위 큐를 사용해야만 하는 문제 (조건3)
# https://claude-u.tistory.com/151
# https://littlefoxdiary.tistory.com/3