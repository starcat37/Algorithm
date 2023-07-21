# 7568

N = int(input())
catalog = []

for _ in range(N):
    weight, height = map(int, input().split(" "))
    catalog.append((weight, height))
    
sortResult = sorted(catalog, reverse=True, key=lambda x: (x[0], x[1]))

grade = []

for i in catalog:
    grade.append(sortResult.index(i))

print(grade)

