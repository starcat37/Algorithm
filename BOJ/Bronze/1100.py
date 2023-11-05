# 1100

white_cnt = 0

for i in range(1, 9):
  line = input()
  if i % 2:
    # 0 2 4 6
    white_squares = line[0] + line[2] + line[4] + line[6]
    white_cnt += white_squares.count("F")
  else:
    # 1 3 5 7
    white_squares = line[1] + line[3] + line[5] + line[7]
    white_cnt += white_squares.count("F")
    
print(white_cnt)
