# 3062

T = int(input())
for _ in range(T):
  num = input()
  reversed_num = num[::-1]
  sum_nums = str(int(num) + int(reversed_num))
  print("YES") if sum_nums == sum_nums[::-1] else print("NO")
