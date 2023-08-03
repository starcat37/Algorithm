# 2759** - dp 점화식 세우는 연습하기...
# https://bio-info.tistory.com/158

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
    
climbs = [0] * (N)

if len(stairs) <= 2:
    print(sum(stairs)) # 계단이 2개 이하: 계단 점수를 모두 합한 게 최대

else:
    climbs[0] = stairs[0] # 첫번째 계단까지의 최대 점수
    climbs[1] = stairs[0] + stairs[1] # 두번째 계단까지의 최대 점수
    for i in range(2, N):
        climbs[i] = max(climbs[i-3] + stairs[i-1] + stairs[i], climbs[i-2] + stairs[i]) # 2계단 연속 걷기, 1계단 건너 뛰기 비교해서 최댓값 계속 갱신
    print(climbs[-1])