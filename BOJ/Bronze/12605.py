# 12605

N = int(input())
for i in range(1, N+1):
    *string_list, = input().split(" ")
    answer = " ".join(string_list[::-1])
    print(f"Case #{i}: {answer}")