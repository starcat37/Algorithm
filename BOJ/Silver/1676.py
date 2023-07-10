# 1676

#재귀함수로 팩토리얼 구하기
def factorial(N):
    if (N > 1):
        return N * factorial(N-1)
    else:
        return 1
    
answer = 0
fac_N = factorial(int(input()))
for i in str(fac_N)[::-1]:
    if i != "0": break
    else: answer += 1
    
print(answer)