#1436

#종말의 수 구해놓기
EndNums = []
i = 0
while True:
    if '666' in str(i):
        EndNums.append(i)
    if len(EndNums) == 10000: break
    i+=1

#입력받고 출력하기
N = int(input())
print(EndNums[N-1])