# 2346

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
ballons = deque(enumerate(list(map(int, input().rstrip().split())), start=1))
order = list()

rotate_cnt = 0

for _ in range(N):
  current = ballons.popleft()
  order.append(current[0])
  
  if ballons:
    rotate_cnt = current[1]
    
    if rotate_cnt > 0: rotate_cnt -= 1 
    # 이미 터진 풍선을 고려해야 하므로 current가 제거된 상태에서의 이동 계산
    # rotate_cnt가 음수일 경우 이미 popleft가 적용되었으므로 rotate_cnt 그대로 사용 
    ballons.rotate(-rotate_cnt)
  
print(" ".join(map(str, order)))
