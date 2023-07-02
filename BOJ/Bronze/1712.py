# 1712

a, b, c = map(int, input().split(" "))
count = 1
#a + b * count < c * count
# a < count * (c - b)

if (c - b <= 0): print(-1)
else:
    print(a // (c - b)+1)