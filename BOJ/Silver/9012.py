#9012**

import sys

T = int(input())
for i in range(T):
    
    stack = []
    string = sys.stdin.readline().strip()
    
    for j in string:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else: #break문으로 끊기지 않고 수행되었을 경우
        if not stack: #스택 비어있음 -> PS
            print("YES")
        else: #t스택에 괄호 있음 -> 매칭 x -> PS 아님
            print("NO")