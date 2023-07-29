# 11399

import sys

N = int(input())
*times, = map(int, sys.stdin.read().split())
cnt = [0] * (N+1)

for i in range(1, N+1):
    short = min(times)
    cnt[i] = short + cnt[i-1]
    times.remove(short)
    
print(sum(cnt))