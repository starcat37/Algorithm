# 9093

T = int(input())
for _ in range(T):
  sen = input()
  result = ""
  for word in list(sen.split(" ")):
    result += word[::-1]+" "
  print(result.rstrip())