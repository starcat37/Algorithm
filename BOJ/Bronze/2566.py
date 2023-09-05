# 2566

board = []
for _ in range(9):
  board.append(list(map(int, input().split())))

result = max(sum(board, []))

print(result)

for row in board:
  if result in row:
    print(board.index(row) + 1, row.index(result) + 1)
    break
  else:
    continue