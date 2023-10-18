# 25192

import sys
input = sys.stdin.readline

N = int(input())
chat_count = {}
gom_count = 0

for _ in range(N):
  message = input().rstrip()
  if message == "ENTER":
    chat_count = {}
  else:
    try:
      chat_count[message] += 1
    except:
      chat_count[message] = 1
      gom_count += 1
  
print(gom_count)