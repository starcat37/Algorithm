# 1406

from collections import deque


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
