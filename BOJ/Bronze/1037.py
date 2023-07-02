#1087

count = int(input())
divisors = list(map(int, input().split()))

if count == 1:
    print(divisors[0] ** 2)
else:
    divisors.sort()
    print(divisors[0] * divisors[-1])
