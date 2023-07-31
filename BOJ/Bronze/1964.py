# 1964**
# https://my-coding-notes.tistory.com/474

N = int(input())
answer = (1+N)*N // 2 # 1부터 N까지의 수의 합
print((answer*3 + N + 1) % 45678)
# N번째 단계의 오각형 점: N*3과 오른쪽 아래의 점 1개