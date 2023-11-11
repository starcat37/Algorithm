# 1406**
# 커서를 기준으로 문자열을 두 deque로 나누어서 생각
# 훨씬 간단하고 직관적인 풀이인 듯... 반성하자

from collections import deque
import sys
input = sys.stdin.readline

left_string = deque(input().rstrip()) # 커서 왼쪽의 문자들 -> 문제 조건: 커서는 문자열 마지막에 위치
right_string = deque() # 커서 오른쪽의 문자들 

M = int(input())

for _ in range(M):
  inst = input().rstrip()
  
  if inst[0] == "L" and left_string:
    right_string.appendleft(left_string.pop())
  elif inst[0] == "D" and right_string:
    left_string.append(right_string.popleft())
  elif inst[0] == "B" and left_string:
    left_string.pop()
  elif inst[0] == "P":
    left_string.append(inst[2])
    
print("".join(left_string) + "".join(right_string))



# 문자열 사이에 구분자를 넣는다고 생각해서 문제인 듯
# '커서 왼쪽'을 인덱스로 저장한다면 굳이 구분자를 거칠 필요가 없지 않을까?
# 이러면 가장 앞 쪽에 커서가 있을 때는? 차라리 커서 오른쪽을 인덱스로 하는 게 맞나
# 시간 초과 + rotate 사용 시 알 수 없는 이유로 틀림

# from collections import deque
# import sys
# input = sys.stdin.readline

# string = deque(input().rstrip())
# N = len(string)
# M = int(input())

# index_right_from_cursor = N

# for _ in range(M):
#   inst = input().rstrip()
#   if inst[0] == "L":
#     index_right_from_cursor = max(0, index_right_from_cursor - 1)
#   elif inst[0] == "D":
#     index_right_from_cursor = min(N, index_right_from_cursor + 1)
#   elif inst[0] == "B":
#     if index_right_from_cursor > 0:
#       string = list(string)
#       string.pop(index_right_from_cursor - 1)
#       string = deque(string)
#       N -= 1
#       index_right_from_cursor -= 1
#   elif inst[0] == "P":
#     string.insert(index_right_from_cursor, inst[2])
#     N += 1
#     index_right_from_cursor += 1

# print("".join(string))


# deque, islice 사용
# 또 시간초과..........
# from collections import deque
# from itertools import islice
# import sys
# input = sys.stdin.readline

# string = "." + (".").join(input().rstrip()) + "."
# text = deque(string)
# M = int(input())
# cursor = len(text) - 1

# for _ in range(M):
#   command = input().rstrip()
#   if command == "L":
#     if cursor != 0:
#       cursor -= 2
#   if command == "D":
#     if cursor != len(text) - 1:
#       cursor += 2
#   if command == "B":
#     if cursor != 0:
#       text = deque("".join(islice(text, 0, cursor-2)) + "".join(islice(text, cursor, len(text))))
#       cursor -= 2
#   if command.startswith("P"):
#     P, string = command.split()
#     string = "." + (".").join(string)
#     text = deque("".join(islice(text, 0, cursor)) + string + "".join(islice(text, cursor, len(text))))
#     cursor += 2
    
# text = "".join(text)
# print(text.replace(".", ""))
