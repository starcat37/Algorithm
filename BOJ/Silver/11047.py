# 11047

# 입력 받기
N, K = map(int, input().split(" "))
cnt = 0
coins = []
for _ in range(N):
    coins.append(int(input()))

# 순서 뒤집기    
coins = coins[::-1]

# value보다 작아질 때까지 나누고 나머지를 재할당
for value in coins:
    while K >= value:
        cnt += (K // value)
        K %= value

# 결과 출력 
print(cnt)