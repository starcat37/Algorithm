#10845

import sys

#기본 큐 정의
queue = []

#입력 받고 경우에 맞게 출력하기
N = int(input())
for i in range(N):
    inst = sys.stdin.readline().strip()
    
    if inst.startswith('push'):
        queue.append(int(inst[5:]))

    elif inst == 'pop':
       if len(queue): 
          print(queue[0])
          del queue[0]
       else:
          print(-1)
        
    elif inst == 'size': print(len(queue))
    
    elif inst == 'empty':
        if len(queue): print(0)
        else: print(1)
    
    elif inst == 'front':
        if len(queue): print(queue[0])
        else: print(-1)
    
    elif inst == 'back':
        if len(queue): print(queue[-1])
        else: print(-1)