# 1158
# 이분 탐색으로 풀기..

import sys
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
lines = []
for _ in range(K):
  lines.append(int(input()))
  
start = 1
end = max(lines) + 1

while start <= end:
  mid = (start + end) // 2
  cnt = 0
  
  for i in lines:
    cnt += i // mid
  
  if cnt < N:
    end = mid - 1
    
  if cnt >= N:
    start = mid + 1
    
print(end)

# 틀렸습니다
# import sys
# input = sys.stdin.readline

# K, N = map(int, input().rstrip().split())
# lines = []
# for _ in range(K):
#   lines.append(int(input()))
  
# cnt = [0] * (min(lines)+1)
# total = 0

# for i in range(1, min(lines)+1):
#   total = 0
#   for j in lines:
#     total += j//i
#   cnt[i] = total
#   if cnt[i] < N:
#     print(i-1)
#     break


# 모든 랜선은 길이가 같아야 함!
# knapsack 문제가 생각나기도 함