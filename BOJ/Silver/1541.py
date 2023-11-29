# 1541

expression = input().split("-")
result = 0

result += sum(list(map(int, expression[0].split("+"))))

for i in expression[1:]:
  for j in i.split("+"):
    result -= int(j)
    
print(result)
