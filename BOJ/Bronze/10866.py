# 10866

cute_cnt = 0
not_cute_cnt = 0

N=int(input())
for _ in range(N):
    opinion = int(input())
    if opinion == 1:
        cute_cnt += 1
    elif opinion == 0:
        not_cute_cnt += 1
        
if cute_cnt > not_cute_cnt:
    print("Junhee is cute!")
else: 
    print("Junhee is not cute!")
