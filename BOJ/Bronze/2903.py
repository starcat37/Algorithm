# 2903
# 4 9(3*3) 25(5*5) 81(9*9)
# 가장 작은 정사각형 기준 변 개수 + 정사각형의 개수
# 점의 개수로만 봤을 때, + 2**n의 수열
# 2(+2**0)3(+2**1)5(+2**2)9(2**3)17(2**4)33...
# 위의 값을 제곱하면 결과

N = int(input())

dots = [2]
counts = [2**i for i in range(16)]

for i in range(N):
  dots.append(dots[i] + counts[i])

print(dots[-1] ** 2)
