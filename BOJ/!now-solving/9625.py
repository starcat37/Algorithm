# 9625

K = int(input())
init = "A"

memo = [(0, 0) for _ in range(K+1)]
memo[0] = (1, 0)

def machine(string, K):
  result = ""
  for c in string:
    if c == "B":
      result += "BA"
    elif c == "A":
      result += "B"
  if K == 0:
    return memo[0]
  if memo[K] != (0, 0):
    return memo[K]
  else:
    return machine(result, K-1)
  
result = machine(init, K)

print(result)


# 1 B 0 1
# 2 BA 1 1
# 3 BAB 1 2
# 4 BABBA 2 3

