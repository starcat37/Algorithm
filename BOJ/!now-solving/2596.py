# 2596

dic = {"000000": "A", "001111": "B", "010011": "C", "011100": "D", "100110": "E", "101001": "F", "110101": "G", "111010": "H"}

N = int(input())
string = input()
result = ""
fail = -1

for i in range(0, N*6, 6):
  part = string[i:i+6]
  try:
    result += dic[part]
  except KeyError:
    one_diffs = []
    for num in dic.keys():
      diff = sum(a != b for a, b in zip(part, num))
      if diff == 1:
        one_diffs.append(num)
    if len(one_diffs) == 1:
      result += dic[one_diffs[0]]
    else:
      fail = i
      break

if fail == -1:
  print(result)
else:
  print(fail//6 + 1)