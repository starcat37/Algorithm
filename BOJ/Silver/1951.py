# 1951

N = input()
cnt = 0

for i in range(1, len(N)+1):
  if i != len(N):
    cnt += i * 9 * (10 ** (i-1))
  else:
    num = int(N) - 10 ** (i-1)
    cnt += i * (num + 1)
  
print(cnt % 1234567)