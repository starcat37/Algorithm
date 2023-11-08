# 1074**
# 분할 정복으로 다시 풀기

def z(N, r, c):
  if N == 0: 
    return 0
  return 2*(r%2)+(c%2) + 4*z(N-1, r//2, c//2)

N, r, c = map(int, input().split())
print(z(N, r, c))

# https://ggasoon2.tistory.com/11