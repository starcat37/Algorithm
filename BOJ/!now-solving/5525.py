# 5525

# KMP 이해하고 풀기
N = int(input())
PN = "O".join(["I" for _ in range(N+1)])

M = int(input())
S = input()

LPS = [0 for _ in range(len(PN))]



# 50점
# import re

# N = int(input())
# PN = "O".join(["I" for _ in range(N+1)])
# regex = "(?=(" + PN + "))"

# M = int(input())
# S = input()

# print(len(re.findall(regex, S)))

# 틀렸습니다
# N = int(input())
# PN = "O".join(["I" for _ in range(N+1)])

# M = int(input())
# S = input()

# cnt = 0
# first = S.index("I") + 1
# current_P = "I"

# for i in range(first, M):
  
#   if current_P[-1] == "O" and S[i] == "I": 
#     current_P += S[i]
  
#   elif current_P[-1] == "I" and S[i] == "O": 
#     current_P += S[i]

#   else:
#     if current_P.count("O") >= N:
#       cnt += len(current_P) // (N+1)
#     current_P = "I"
    
# print(cnt)
