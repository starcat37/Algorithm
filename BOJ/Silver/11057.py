# 11057

N = int(input())
cnt = 0

if N == 1:
    cnt = 10
else:
    for i in range(10**(N-1), 10**N):
        i_list = list(map(int, str(i)))
        print(i_list)
        if all(i_list[j] <= i_list[j+1] for j in range(N-1)):
            cnt += 1
            print(cnt)
            
print(cnt%10007)

# 결과값 이상함, 0부터 시작할 수 있다가 이상함