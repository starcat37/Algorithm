#11866

import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))

people = [i for i in range(1, N)]
permutation = []
start = 0

for i in range(N):
    if (start + K - 1> N): 
        start -= N
    permutation.append(people[start + K - 1])
    print(start)
    start += K
    print(start)
    print(permutation)