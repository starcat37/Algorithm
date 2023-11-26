# 5789

N = int(input())
for _ in range(N):
  string = input()
  length = len(string)//2
  print("Do-it") if string[length-1] == string[length] else print("Do-it-Not")
