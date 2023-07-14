# 1094

X = int(input())
sticks = [64, ]

while True:
    if sum(sticks) == X:
        break
    else:
        shortest = min(sticks)
        sticks.remove(shortest)
        half = shortest // 2
        sticks.append(half)
        sticks.append(half)
        if sum(sticks) - half >= X:
            sticks.remove(half)

print(len(sticks))