# 9506

import math

while True:
  num = int(input())
  divisor = []
  if num == -1:
    break
  for i in range(1, math.ceil(math.sqrt(num))):
    if num % i == 0:
      divisor.append(i)
      divisor.append(num//i)
  divisor.sort()
  
  if sum(divisor[:-1]) == num:
    result = " + ".join(map(str, divisor[:-1]))
    print(f"{num} = {result}")
  else:
    print(f"{num} is NOT perfect.")