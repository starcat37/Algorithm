# 1003

cnt_0 = 0
cnt_1 = 0
fibos = {0:0, 1:1}

def Fibo_cnt(n):
    if n == 0:
        global cnt_0
        cnt_0 += 1
    if n == 1:
        global cnt_1
        cnt_1 += 1
    if n in fibos:
        return fibos[n]
    fibos[n] = Fibo_cnt(n-1) + Fibo_cnt(n-2)
    return fibos[n]
    
    
T = int(input())
for _ in range(T):
    Fibo_cnt(int(input()))
    print(cnt_0, cnt_1)
    cnt_0, cnt_1 = 0, 0