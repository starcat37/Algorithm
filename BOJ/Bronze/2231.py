#2231

#생성자 찾기 함수 정의
def FindGen(N):
    for i in range(N):
        if i + sum(list(map(int, list(str(i))))) == N: 
            return i

#입력받기
N = int(input())

#생성자가 없을 경우 0 출력하도록 조건문
answer = FindGen(N)
if answer: print(answer)
else: print(0)