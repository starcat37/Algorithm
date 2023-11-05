# 28279

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deque = deque([])

for _ in range(N):
  inst = list(map(int, input().split()))
  inst_type = inst[0]
  if inst_type == 1:
    deque.appendleft(inst[1])
  elif inst_type == 2:
    deque.append(inst[1])
  elif inst_type == 3:
    print(deque.popleft()) if deque else print(-1)
  elif inst_type == 4:
    print(deque.pop()) if deque else print(-1)
  elif inst_type == 5:
    print(len(deque))
  elif inst_type == 6:
    print(0) if deque else print(1)
  elif inst_type == 7:
    print(deque[0]) if deque else print(-1)
  elif inst_type == 8:
    print(deque[-1]) if deque else print(-1)
