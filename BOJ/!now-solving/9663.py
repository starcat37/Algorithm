# 9663**
# 백트래킹

# 백트래킹 함수
def backtrack(k): # k: 체스판의 시작 행
  global cnt
  for i in range(N):
    if queen(k, i):
      board[k] = i
      if k == N-1:
        cnt += 1
        return
      else:
        backtrack(k+1)

# 유망 조건
def queen(a, b): # (a, b)는 현재 퀸을 놓으려는 위치
  for i in range(a):
    # 같은 열이거나 같은 대각선(변화량)
    if board[i] == b or abs(board[i]-b) == abs(i-a):
      return False
  return True

N = int(input())
board = [0] * N
cnt = 0
backtrack(0)
print(cnt)
