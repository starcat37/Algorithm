#10250

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(" "))
    floor = N % H  #층수
    room = N // H + 1 #방 번호

    if floor == 0:
        floor = H #N이 H로 딱 떨어질 경우 층수는 H
        room = N // H #방 번호도 하나 빼줌

    if room < 10:
        print(str(floor) + "0" + str(room))
    else:
        print(str(floor) + str(room))