#1920

import sys

def binarySearch(arr, start, end, target):
    if start > end:
        return False
    mid = (start + end) // 2

    if (arr[mid] == target):
        return True
    elif (arr[mid] > target):
        return binarySearch(arr, start, mid-1, target)
    else:
        return binarySearch(arr, mid+1, end, target)

#입력 받기
N = int(input())
N_list = sorted(list(map(int, sys.stdin.readline().split(" "))))
M = int(input())
M_list = list(map(int, sys.stdin.readline().split(" ")))

#Binary Search 사용
for i in M_list:
    result = binarySearch(N_list, 0, N-1, i)
    if result: 
        print(1)
    else: 
        print(0)