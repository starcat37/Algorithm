# 1822

N_A, N_B = map(int, input().split(" "))
*A, = map(int, input().split(" "))
*B, = map(int, input().split(" "))

print(len(set(A) - set(B)))
if (len(set(A) - set(B))):
    print(" ".join(list(map(str, sorted(set(A) - set(B))))))
