# 11931

numbers = []

N = int(input())
for _ in range(N):
  numbers.append(int(input()))
  
numbers.sort(reverse=True)

for num in numbers:
  print(num)
