#11866**

import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))

people = [i for i in range(1, N+1)]
permutation = []
start = K-1

while True:
    permutation.append(people[start])
    people.remove(people[start])
    if not len(people):
        break
    start += K -1
    if start >= len(people):
        start %= len(people)

permutation = map(str, permutation)
print("<" + ", ".join(permutation) + ">")