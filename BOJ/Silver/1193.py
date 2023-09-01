# 1193**

X = int(input())

line = 0
max_num = 0
while X > max_num:
  line += 1
  max_num += line

diff = max_num - X
if line % 2 == 0:
  num1 = line - diff
  num2 = diff + 1
else:
  num1 = diff + 1
  num2 = line - diff
  
print(num1, "/" , num2, sep="")