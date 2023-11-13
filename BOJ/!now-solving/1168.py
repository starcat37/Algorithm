# 1168

"""
세그먼트 트리에 i~j번 사람들 중 빠진 사람의 수를 저장하자. 
이후 사람을 찾을 때 이전에 빠진 사람보다 번호가 더 큰 사람들 중 빠질 사람이 있는지 확인하고, 
만일 없다면 번호가 더 작은 사람들 중 빠질 사람을 찾는다.
"""

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
