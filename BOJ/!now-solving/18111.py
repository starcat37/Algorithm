# 18111

import sys
input = sys.stdin.readline

# 입력 받기
N, M, B = map(int, input().rstrip().split(" "))
ground = []
for i in range(N):
    ground.append(list(map(int, input().rstrip().split(" "))))

print(ground)



# 블록 제거 + 블록 위에 놓기가 혼합되는 경우
# 땅의 높이는 256블록까지, 음수가 될 수 없음
# 그냥 리터럴리 구현하는 건가?