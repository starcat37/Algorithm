# 7785

log = {}
n = int(input())

for _ in range(n):
  name, status = map(str, input().split())
  log[name] = status

for name in sorted(log.keys(), reverse=True):
  if log[name] == "enter":
    print(name)