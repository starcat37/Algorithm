#2164

from collections import deque

#입력받기
N = int(input())
cards = deque([i for i in range(1, N+1)])

#동작 정의
def act(cards):
    while (len(cards) != 1):
        cards.popleft()
        cards.append(cards[0])
        cards.popleft()
    print(cards[0])

act(cards)