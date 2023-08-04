# 1816

N = int(input())

# 1000000 이전의 소수 구하기
primes = set(range(2, 1000001))
for i in range(2, 1000001):
    if i in primes:
        primes -= set(range(2*i, 1000001, i))
        
for _ in range(N):
    isBad = 0
    num = int(input())
    for prime in primes:
        if num % prime == 0:
            isBad += 1
            print("NO")
            break
        else:
            continue
    if isBad == 0:
        print("YES")
    
        
# def factorize(num):
#     fac_num = []
#     d = 2 #첫 소수
#     while d <= int(math.sqrt(num)):
#         if num % d == 0: # 약수일 경우
#             if d < 1000000:
#                 break
#             fac_num.append(d)
#             num //= d
#         else: # 약수가 아닐 경우
#             d += 1
#     return fac_num
            
#     fac_num = factorize(num)
#     if len(fac_num) == 0 or min(fac_num) <= 1000000:
#         print("NO")
#     else:
#         print("YES")