# 24511

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
types = list(map(int, input().split()))
inits = list(map(int, input().split()))
M = int(input())
elements = list(map(int, input().split()))

# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# # 번호: deque 형태의 딕셔너리

# types = list(map(int, input().split()))
# inits = list(map(int, input().split()))
# M = int(input())
# elements = list(map(int, input().split()))

# # 초깃값 정의
# queuestack = dict()
# for i in range(N):
#   queuestack[i] = (types[i], deque([inits[i]]))

# print(queuestack)
  
# # 각 주어진 요소들 삽입
# for j in range(M):
#   for k in range(N):
#     pass
# # O(N^2)? 다시 생각해보기
