# 11052

N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [-1 for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
  for j in range(1, i+1):
    if dp[i] == -1: # 아직 계산하지 않은 경우
      dp[i] = dp[i-j] + cards[j]
    else:
      dp[i] = max(dp[i], dp[i-j] + cards[j])
  
print(dp[N])

# 각 예제에 대한 dp 값을 전개해보고, 점화식을 유추해본 건 발전한 듯 하다
# 그러나 아직 완벽한 점화식은 못 세웠다. i번째일 때의 dp값은 cards[i]와 이전 값들을 합한 dp값 중 큰 값이라고 러프하게 추측했지만, 정확한 식은 못 세웠다.
# 경우의 수가 i가 증가할 수록 늘어난다는 점을 캐치해서 j 값을 가져와 그때마다 dp를 계산하는 for문을 세울 수 있다는 점을 배웠다.
# 이건 2차원 리스트로 표현이 가능해보인다.