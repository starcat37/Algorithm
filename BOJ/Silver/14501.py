# 14501** - 그리디 아님... DP임

catalog = []

N = int(input())
for i in range(N):
    a, b = map(int, input().split(" "))
    catalog.append([a, b])

revenue = [0] * (N+1)

for i in range(N):
    for j in range(i+catalog[i][0], N+1):
        if revenue[j] < revenue[i] + catalog[i][1]:
            revenue[j] = revenue[i] + catalog[i][1]
    
print(max(revenue))
