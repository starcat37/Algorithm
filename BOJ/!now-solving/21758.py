# 21758

"""
꿀통을 좌우 끝이 아닌 곳에 둔다면 벌들은 항상 양쪽 끝에 하나씩 놓는 것이 최선이고, 
꿀통을 좌측 끝 또는 우측 끝에 둔다면 두 벌 중 하나는 항상 왼쪽 끝에 놓는 것이 최선이다. 
이제 꿀통이나 벌을 옮겨가며, 얻을 수 있는 꿀의 양을 이분 탐색으로 계산하자.
"""

# 꿀통이 좌측/우측 끝에 있는 경우 -> 벌 한 마리는 맨 끝, 한 마리는 나머지 중 최소값
# 여기도 누적합 앞뒤로 하나씩 필요

# 꿀통이 좌우 끝이 아닌 곳에 있는 경우 -> 벌들은 항상 맨 끝에
# 앞에서부터 시작하는 누적합, 뒤에서부터 시작하는 누적합 1개씩

# 앞뒤 누적합을 하나씩 구하고 시작

import sys
input = sys.stdin.readline

N = int(input())
sites = list(map(int, input().rstrip().split()))

beehive = 0
bee_1 = 0
bee_2 = 0

max_honey_amount = 0

# 앞뒤 누적합 구하기
prefix_sum_front = [0] * (N+1)
prefix_sum_back = [0] * (N+1)

for i in range(N):
  prefix_sum_front[i+1] = prefix_sum_front[i] + sites[i]

sites_back = sites[::-1]

for i in range(N):
  prefix_sum_back[i+1] = prefix_sum_back[i] + sites_back[i]

prefix_sum_front = prefix_sum_front[1:]
prefix_sum_back = prefix_sum_back[1:]

# bee_2의 index 미리 찾기
bee_2_beehive_leftmost = 0
bee_2_beehive_rightmost = 0

min_value = min(sites[1:-1])
min_indices = [i for i, x in enumerate(sites[1:-1], start=1) if x == min_value]
# 단순하게 탐색하는 걸로ㄱㄱ

bee_2_beehive_leftmost = min_indices[-1]
bee_2_beehive_rightmost = min_indices[0]

# 꿀통을 옮기면서 벌들의 위치도 변경, 최대 꿀 양 변경
for i in range(N):
  beehive = i
  if beehive == 0:
    bee_1 = N-1
    bee_2 = bee_2_beehive_leftmost
    
    bee_1_honey_amount = prefix_sum_back[beehive] - sites[bee_1] - sites[bee_2]
    bee_2_honey_amount = prefix_sum_back[beehive] - prefix_sum_back[bee_2]
    
    total_honey_amount = bee_1_honey_amount + bee_2_honey_amount
    
    if total_honey_amount > max_honey_amount: max_honey_amount = total_honey_amount

  elif beehive == N-1:
    bee_1 = 0
    bee_2 = bee_2_beehive_rightmost
    
    bee_1_honey_amount = prefix_sum_front[beehive] - sites[bee_1] - sites[bee_2]
    bee_2_honey_amount = prefix_sum_front[beehive] - prefix_sum_front[bee_2]
    
    total_honey_amount = bee_1_honey_amount + bee_2_honey_amount
    
    if total_honey_amount > max_honey_amount: max_honey_amount = total_honey_amount

  else:
    bee_1 = 0
    bee_2 = N-1
    
    bee_1_honey_amount = prefix_sum_front[beehive] - sites[bee_1]
    bee_2_honey_amount = prefix_sum_back[beehive] - sites[bee_2]
    
    total_honey_amount = bee_1_honey_amount + bee_2_honey_amount
    
    if total_honey_amount > max_honey_amount: max_honey_amount = total_honey_amount

# 결과 출력
print(max_honey_amount)
