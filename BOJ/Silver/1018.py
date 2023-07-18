# 1018**

M, N = map(int, input().split(" "))
board = []
for _ in range(M):
    board.append(input())
count = []

for a in range(M - 7):
    for b in range(N - 7):
        index_white = 0
        index_black = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 짝수인 경우
                    if board[i][j] != "W":
                        index_white += 1 # W로 칠하는 개수
                    if board[i][j] != "B":
                        index_black += 1 # B로 칠하는 개수
                else: # 홀수인 경우
                    if board[i][j] != "W":
                        index_black += 1 # B로 칠하는 개수
                    if board[i][j] != "B":
                        index_white += 1 # W로 칠하는 개수
        count.append(index_white)
        count.append(index_black)
        
print(min(count))