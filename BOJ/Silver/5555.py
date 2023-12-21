# 5555

target = input()
N = int(input())
cnt = 0

for _ in range(N):
  pattern = input()
  ring_pattern = pattern*2
  if target in ring_pattern:
    cnt += 1

print(cnt)
