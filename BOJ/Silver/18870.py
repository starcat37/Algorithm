# 18870*
# dict으로 대응쌍 찾는 시간 복잡도 O(1)

import sys
input = sys.stdin.readline

N = int(input())
coordinates = list(map(int, input().rstrip().split()))
c_set = sorted(set(coordinates))

c_dict = {}
for i in range(len(c_set)):
  c_dict[c_set[i]] = i
  
for i in coordinates:
  print(c_dict[i], end=" ")

# 18870
# # dict으로 대응쌍 찾는 시간 복잡도 O(1)

# import sys
# input = sys.stdin.readline

# N = int(input())
# coordinates = list(map(int, input().rstrip().split()))
# c_set = sorted(set(coordinates)) # -10 -9 2 4

# c_dict = {}
# for i in range(len(c_set)): # i: 0 1 2 3
#   c_dict[c_set[i]] = i # -10:0, -9:1, 2:2, 3:3
  
# for i in coordinates: # 2 4 -10 4 -9
#   print(c_dict[i], end=" ") # 2 3 0 3 1


# 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# coordinates = list(map(int, input().rstrip().split()))
# result = [0 for _ in range(N)]

# num_types = sorted(set(coordinates))

# for i in range(N):
#   result[i] = num_types.index(coordinates[i])
      
# print(" ".join(map(str, result)))
