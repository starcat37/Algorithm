# 10811 

N, M = map(int, input().split())
baskets = [str(i) for i in range(1, N+1)]
for _ in range(M):
  i, j = map(int, input().split())
  baskets = baskets[:i-1] + baskets[i-1:j][::-1] + baskets[j:]
print(" ".join(baskets))