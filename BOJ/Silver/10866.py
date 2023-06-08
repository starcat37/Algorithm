#10866

import sys

#기본 덱 정의
deque = []

#입력 받고 경우에 맞게 출력하기
N = int(input())
for i in range(N):
    inst = sys.stdin.readline().strip()
    
    if inst.startswith('push_front'):
        deque.insert(0, int(inst[11:]))

    elif inst.startswith('push_back'):
        deque.append(int(inst[10:]))

    elif inst == 'pop_front':
       if len(deque): 
            print(deque[0])
            del deque[0]
       else: print(-1)

    elif inst == 'pop_back':
        if len(deque):
            print(deque[-1])
            del deque[-1]
        else: print(-1)
        
    elif inst == 'size': print(len(deque))
    
    elif inst == 'empty':
        if len(deque): print(0)
        else: print(1)
    
    elif inst == 'front':
        if len(deque): print(deque[0])
        else: print(-1)
    
    elif inst == 'back':
        if len(deque): print(deque[-1])
        else: print(-1)
