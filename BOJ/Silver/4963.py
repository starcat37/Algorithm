# 4963

import sys
sys.setrecursionlimit(10 ** 4)

# DFS 정의하기
dy = (-1, -1, -1, 1, 1, 1, 0, 0)
dx = (-1, 0, 1, -1, 0, 1, -1, 1)
def DFS(y, x):
    visited[y][x] = True
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny][nx] and chart[ny][nx]:
                DFS(ny, nx)

# 입력 받고 실행하기
while (True):
    w, h = map(int, sys.stdin.readline().split(" "))
    if w == 0 and h == 0:
        break
    chart = []
    for _ in range(h):
        *row, = map(int, input().split(" "))
        chart.append(row)
    
    land_cnt = 0
    visited = [[False] * w for _ in range(h)] # 방문 목록
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and chart[i][j]: # 방문하지 않았고 land일 경우
                DFS(i, j)
                land_cnt += 1 # 새로운 섬 개수 카운트
    
    print(land_cnt)
