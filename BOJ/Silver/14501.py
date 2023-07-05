# 14501 - 그리디 아님

catalog = [[0, 0]]

N = int(input())
for i in range(N):
    a, b = map(int, input().split(" "))
    catalog.append([a, b])

revenue = []

for i in range(1, N+1):
    result = 0
    k = i
    while k <= N:
        if k + catalog[k][0] > N:
            break
        else:
            result += catalog[k][1]
            k += catalog[k][0]
    revenue.append(result)
    
print(max(revenue))