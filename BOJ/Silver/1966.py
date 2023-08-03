# 1966** -> 기존 큐에서의 위치를 반영해야 함
# pop으로 열심히 짰는데 짜증남ㅠ
# https://hongcoding.tistory.com/42

from collections import deque

def priority_queue(M, priorities):
    cnt = 0
    while priorities:
        best = max(priorities)
        front = priorities.popleft()
        M -= 1
        
        if best == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            priorities.append(front)
            if M < 0:
                M = len(priorities) - 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split(" "))
    priorities = deque(list(map(int, input().split(" "))))
    result = priority_queue(M, priorities)
