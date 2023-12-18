# 30979

T = int(input())
N = int(input())
F_list = list(map(int, input().split()))

print("Padaeng_i Happy") if sum(F_list) >= T else print("Padaeng_i Cry")
