# 4375

while True:
  try:
    N = int(input())
    num = 1
    while True:
      if num % N != 0:
        num = int(str(num) + "1")
        continue
      else:
        print(len(str(num)))
        break
  except EOFError:
    break
