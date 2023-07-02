#11653

N = int(input())

def factorize(N):
    d = 2 #첫 소수
    while d <= N: #d가 N보다 커지면 나눌 수 없으므로
        if N % d == 0: # 약수일 경우
            print(d)
            N = N / d
        else: # 약수가 아닐 경우
            d += 1
            
factorize(N)