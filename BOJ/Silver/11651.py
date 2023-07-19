# 11651

dots = []

N = int(input())
for _ in range(N):
    x, y = map(int, input().split(" "))
    dots.append((x, y))

result = sorted(dots, key=lambda x: (x[1], x[0]))
for i in result:
    print(i[0], i[1])