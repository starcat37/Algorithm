# 15663

from itertools import permutations

N, M = map(int, input().split())
*N_list, = list(map(int, input().split()))
N_list.sort()
perms = list(permutations(N_list, M))

result = []
for perm in perms:
  result.append(perm)

result = sorted(list(set(result)))

for i in result:
  print(*i)