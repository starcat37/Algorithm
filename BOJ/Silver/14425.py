# 14425

N, M = map(int, input().split())
S = []
cnt = 0
for _ in range(N):
  S.append(input())
  
for _ in range(M):
  string = input()
  if string in S:
    cnt += 1
    
print(cnt)