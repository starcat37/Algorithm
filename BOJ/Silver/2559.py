# 2559

# 2559

import sys
input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().rstrip().split())
temps = list(map(int, input().rstrip().split()))

# 누적합 구하기
culmulated_temps = [0] * (N+1)
for i in range(N):
  culmulated_temps[i+1] = culmulated_temps[i] + temps[i]

# K일 간의 최댓값 구하기
max_temp = float('-inf')
for i in range(K-1, N):
  cur_temp = culmulated_temps[i+1] - culmulated_temps[i+1-K]
  if max_temp < cur_temp: max_temp = cur_temp
  
# 결과 출력
print(max_temp)
