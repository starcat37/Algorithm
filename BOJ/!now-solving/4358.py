# 4358

from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])
result = []

while cards:
  result.append(cards.popleft())
  cards.rotate(-1)

print(" ".join(map(str, result)))
