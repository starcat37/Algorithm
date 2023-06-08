#11656

#입력받기
S = input()

#접미사 목록 및 인덱스 정의
suffixes = []
i = -1

#접미사 목록에 추가
for i_ in range(len(S)):
    suffixes.append(S[i:])
    i -= 1

#출력하기
for j in sorted(suffixes):
    print(j)