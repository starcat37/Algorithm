# 1012

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# DFS
def DFS(ground, start):
  for i in range(4):
    


# 입력받기
import sys
input = sys.stdin.readline

T = int(input())
M, N, K = map(int, input().split())
ground = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
  X, Y = map(int, input().split())
  ground[X][Y] = 1

# 


