# 1620
# 반복해서 값을 받을 경우 readline 사용하기, input()은 느림!

import sys

pokemon = {}

N, M = map(int, input().split(" "))
for cnt in range(1, N+1):
    pokemon[cnt] = sys.stdin.readline().strip()

reversed_pokemon = dict(map(reversed, pokemon.items()))

for _ in range(M):
    question = sys.stdin.readline().strip()
    if question.isdecimal():
        print(pokemon[int(question)])
    else:
        print(reversed_pokemon[question])