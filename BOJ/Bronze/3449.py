# 3449

T = int(input())
for _ in range(T):
    ham = 0
    a = input()
    b = input()
    for i in range(len(a)):
        if a[i] != b[i]: ham += 1
        else: continue
    print(f"Hamming distance is {ham}.")