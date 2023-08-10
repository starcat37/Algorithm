# 2606

network = {}
cnt = int(input())
for i in range(1, cnt+1):
    network[i] = []
pair = int(input())

for _ in range(pair):
    a, b = map(int, input().split(" "))
    network[a].append(b)
    network[b].append(a)
    
virus = [1]
for i in virus:
    if len(set(virus)) > pair:
        break
    virus.extend(network[i])
    
print(list(set(virus)))