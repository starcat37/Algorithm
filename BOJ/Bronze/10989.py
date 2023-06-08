#10989**

import sys

#입력 받기
input = sys.stdin.readline
N = int(input())
counts = [0] * 10001

#해당하는 수의 자릿수 증가
for i in range(N):
    counts[int(input())] += 1

#자릿수만큼 반복하여 출력하기
for input_num in range(1, 10001):
    if counts[input_num] != 0: 
        for _ in range(counts[input_num]):
            print(input_num)