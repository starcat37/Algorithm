# 16929

def DFS(x, y, cnt, color, start):
  global answer
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if answer:
      return
    if 0 <= nx < N and 0 <= ny < M:
      if cnt >= 4 and start[0] == nx and start[1] == ny:
        answer = True
        return
      if visited[nx][ny] == 0 and gameboard[nx][ny] == color:
        visited[nx][ny] = 1
        DFS(nx, ny, cnt+1, color, start)
        visited[nx][ny] = 0
  return False
    
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
gameboard = []
visited = [[0] * M for _ in range(N)]
answer = False
for _ in range(N):
  gameboard.append(list(input().rstrip()))
  
for i in range(N):
  for j in range(M):
    start = (i, j)
    visited[i][j] = True
    DFS(i, j, 1, gameboard[i][j], start)

if answer:
  print("Yes")
else:
  print("No")

# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-16929%EB%B2%88-Two-Dots-%EC%B4%88%EC%BD%94%EB%8D%94
