#2751

import sys

#N 입력받기
num = int(sys.stdin.readline().strip())
num_list = []

#수 입력받기
for i in range(num):
    num_list.append(int(sys.stdin.readline().strip()))

#정렬하고 출력
num_list.sort()
for i in num_list: print(i)