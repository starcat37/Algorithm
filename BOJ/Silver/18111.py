# 18111**

import sys
input = sys.stdin.readline

# 입력 받기
N, M, B = map(int, input().rstrip().split(" "))
ground = []
for i in range(N):
    ground.extend((map(int, input().rstrip().split(" "))))

times = [0 for i in range(257)]
height = 0

for h in range(257):
    block = B 
    for i in ground:
        if i <= h:
            times[h] += h - i
            block -= h - i
        else:
            times[h] += 2 * (i - h)
            block += i - h
    if block >= 0 and times[h] <= times[height]: # 오름차순으로 순회하므로 그 중 높이가 가장 높은 걸 할당
        height = h # 최소 소요 시간인 높이 저장
    
print(times[height], height)
    
# 참고: https://velog.io/@minjungh63/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-18111%EB%B2%88

# python3 시간 초과, pypy 틀렸습니다.
# import sys
# input = sys.stdin.readline

# # 입력 받기
# N, M, B = map(int, input().rstrip().split(" "))
# ground = []
# cur_B = B
# for i in range(N):
#     ground.extend(list(map(int, input().rstrip().split(" "))))

# result = []

# for i in range(257):
#     time = 0
#     is_out = 1
#     cur_B = B
#     for j in ground:
#         if i < j:
#             time += 2 * (j - i)
#             cur_B += j - i
#         if i > j:
#             time += i - j
#             cur_B -= i - j
#             if cur_B < 0:
#                 is_out = 0
#                 break
#         else:
#             pass
#     if is_out:
#         result.append((time, i))

# print(" ".join(map(str, min(result, key = lambda x: (x[0], -x[1])))))


# 블록 제거 + 블록 위에 놓기가 혼합되는 경우
# 땅의 높이는 256블록까지, 음수가 될 수 없음
# 그냥 리터럴리 구현하는 건가?

# 걸리는 시간과 땅의 높이...
# 땅의 높이가 i가 되도록 다듬거나 제거하는 최소 시간