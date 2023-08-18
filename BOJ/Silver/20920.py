# 20920

import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().rstrip().split(" "))
words = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

# 단어장 만들기
voca_list = sorted(words.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for i in voca_list:
    print(i[0])


# 시간 초과
# import sys

# # 입력 받기
# N, M = map(int, sys.stdin.readline().rstrip().split(" "))
# words = []
# for _ in range(N):
#     word = sys.stdin.readline().rstrip()
#     if len(word) >= M:
#         words.append(word)

# # 단어장 만들기
# # 람다식 활용과 아스키 코드 활용!
# voca_list = sorted(words, reverse=True, key= lambda x: (words.count(x), len(x), -sum(ord(c) for c in x)))
# voca_list = sorted(set(voca_list), key = lambda x: voca_list.index(x))

# # 출력
# for i in voca_list:
#     print(i)