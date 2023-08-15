# 14467

cnt = 0
record = {}

N = int(input())
for _ in range(N):
    a, b = map(int, input().split(" "))
    if (record.get(a) == 0 and b == 1) or (record.get(a) == 1 and b == 0):
        cnt += 1
        record[a] = b
    else:
        record[a] = b
        
print(cnt)