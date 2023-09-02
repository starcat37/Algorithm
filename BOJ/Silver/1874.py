# 1874**
# https://hongcoding.tistory.com/39
# TOP 값이 입력한 숫자보다 크면, 
# 입력한 수를 꺼내기 위해 계속 POP을 해야 하기 때문에 그 과정에서 pop한 수들의 수열이 달라짐

n = int(input())
stack = []
answer = []
available = 1
now = 1
for _ in range(n):
    num = int(input())
    while now <= num: # 주어진 수를 만날 때까지 push
        stack.append(now)
        answer.append("+")
        now += 1
    
    if stack[-1] == num: # TOP이 해당 수일 경우 -> pop
        stack.pop()
        answer.append("-")
    else: # TOP이 해당 수가 아닐 경우 -> 불가능
        available = 0
        print("NO")
        break

if available:
    for i in answer:
        print(i)