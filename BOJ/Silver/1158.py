# 1158
# deque 회전으로 풀이

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

people = deque([i for i in range(1, N+1)])
result = []

people.rotate(-K)

while people:
  result.append(people.pop())
  people.rotate(-K)

print("<" + ", ".join(map(str, result)).rstrip() + ">")
