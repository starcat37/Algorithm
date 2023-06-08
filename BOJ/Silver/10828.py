#10828

import sys

#기본 스택 정의
stack = []

#입력 받고 경우에 맞게 출력하기
N = int(input())
for i in range(N):
    inst = sys.stdin.readline().strip()
    
    if inst.startswith('push'):
        stack.append(int(inst[5:]))

    elif inst == 'pop':
       if len(stack): 
          print(stack[-1])
          del stack[-1]
       else:
          print(-1)
        
    elif inst == 'size': print(len(stack))
    
    elif inst == 'empty':
        if len(stack): print(0)
        else: print(1)
    
    elif inst == 'top':
        if len(stack): print(stack[-1])
        else: print(-1)