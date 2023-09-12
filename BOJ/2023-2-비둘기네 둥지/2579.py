# 2579

# 입력 받기
n = int(input())
stairs = [0] # '번째'로 보기 위해 0 미리 설정
for _ in range(n):
  stairs.append(int(input()))

dp = [0] * (n+1) # dp 리스트(메모이제이션?)

dp[1] = stairs[1] # 첫 계단 오름
if n > 1:
  dp[2] = stairs[1] + stairs[2] # 두 번째 계단 오름(2번째 계단에서의 최댓값)
if n > 2:
  dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) # 3번째 계단 오르기 (3번쨰 계단에서의 최댓값)
if n > 3:
  for i in range(4, n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]) # i번째 계단에서의 최댓값
  
# 조건을 고려하여, i번째 계단을 오를 때 1) i-2번쨰에서 2칸 2) i-1번째에서 1칸 오르는 경우 있음
# 이 때 1)의 경우, i-2번째 계단까지의 최댓값 + i번째 계단 값 = i번째 계단까지의 최댓값
# 2)의 경우, 3번 연속 1칸 오르기가 불가능하므로, 반드시 i-3번째 계단에서 출발한 것임. 즉, 점화식은 i-3번째 계단까지의 최댓값 + i-1번째 계단 값 + i번째 계단 값
# 해당 점화식을 식으로 세우면 다음과 같음: max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# 마지막 계단을 반드시 밟는 것은 i값이 n까지 for문을 돌기 때문임

print(dp[-1]) # 가장 마지막 계단에서의 dp 값 = 최댓값

"""
전형적인 dp문제로, 점화식을 세워 풀 수 있다.



조건을 고려하면, i번째 계단을 오를 때 1) i-2번쨰에서 2칸 오르는 경우, 2) i-1번째에서 1칸 오르는 경우가 있다.

1)의 경우, i-2번째 계단까지의 최댓값 + i번째 계단 값 = i번째 계단까지의 최댓값이다/

2)의 경우, 3번 연속 1칸씩 오를 수 없고, 이미 1칸씩 2번 올라 총 2칸을 오른 상태이므로, 직전에 i-3번째 계단에서 2칸 올라 i-1번째 계단에 있는 것임을 알 수 있다. 

즉, 점화식은 i-3번째 계단까지의 최댓값 + i-1번째 계단 값 + i번째 계단 값이다.



해당 점화식을 코드로 작성하면 다음과 같다. 

max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
두 경우 중 큰 값이 i번째 계단까지의 최댓값이다.



마지막 계단을 반드시 밟아야 한다는 조건은 i값에 대한 for loop가 마지막(n번째) 계단인 n까지 돌기 때문에 반드시 성립한다.



참고: https://v3.leedo.me/devs/64
"""

# N = int(input())
# stairs = []
# for _ in range(N):
#   stairs.append(int(input()))

# pos = 0
# one_cnt = 0

# memo = [0, stairs[-1]]
# stairs_reversed = stairs[::-1]


# while True:
#   if pos >= len(stairs_reversed) - 1:
#     break
#   elif pos == len(stairs_reversed) - 2:
#     memo.append(memo[-1] + stairs_reversed[pos + 1])
#     break
#   elif one_cnt == 3:
#     two_down = memo[-1] + stairs_reversed[pos + 2]
#     memo.append(two_down)
#     pos += 2
#     one_cnt = 0
#   else:
#     one_down = memo[-1] + stairs_reversed[pos + 1]
#     two_down = memo[-1] + stairs_reversed[pos + 2]
#     if one_down >= two_down:
#       memo.append(one_down)
#       pos += 1
#       one_cnt += 1
#     else:
#       memo.append(two_down)
#       pos += 2
#       one_cnt = 0

# print(memo[-1])