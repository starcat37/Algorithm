# 2776

T = int(input())
for _ in range(T):
  N = int(input())
  note_1 = {i:0 for i in range(1, N+1)}
  note_1_nums = list(map(int, input().split()))
  for n in note_1_nums:
    note_1[n] = 1
  
  M = int(input())
  note_2_nums = list(map(int, input().split()))
  for n in note_2_nums:
    try:
      result = note_1[n]
      if result: print(1)
      else: print(0)
    except KeyError:
      print(0)

# 이분탐색, KeyError