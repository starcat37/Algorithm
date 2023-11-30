# 11383

N, M = map(int, input().split())

input_strings = []
answer_strings = []

for _ in range(N):
  input_strings.append(input())
  
for _ in range(N):
  answer_strings.append(input())
  
result = ""
for string in input_strings:
  for s in string:
    result += s*2

answer = "".join(answer_strings)

print("Eyfa") if result == answer else print("Not Eyfa")
