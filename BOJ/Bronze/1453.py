# 1453

N = int(input())
customers = list(map(int, input().split()))
print(len(customers) - len(set(customers)))