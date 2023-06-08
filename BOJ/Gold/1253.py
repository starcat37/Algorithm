#1253

import sys

#입력 받기
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split(' ')))
count = 0
A.sort()

#투 포인터
for k in range(N):
    target = A[k]
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == target:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1

print(count)