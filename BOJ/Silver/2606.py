# 2606

def DFS(v, virus = []):
    virus.append(v)
    for i in network[v]:
        if not i in virus:
            virus = DFS(i, virus)
    return virus

network = {}
cnt = int(input())
for i in range(1, cnt+1):
    network[i] = []
pair = int(input())

for _ in range(pair):
    a, b = map(int, input().split(" "))
    network[a].append(b)
    network[b].append(a)

result = DFS(1, virus=[])
print(len(result)-1)