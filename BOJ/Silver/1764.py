# 1764

not_heard = set()
not_seen = set()

N, M = map(int, input().split())
for _ in range(N):
    not_heard.add(input())

for _ in range(M):
    not_seen.add(input())
    
not_heard_seen = sorted(not_heard.intersection(not_seen))

print(len(not_heard_seen))
for i in not_heard_seen:
    print(i)