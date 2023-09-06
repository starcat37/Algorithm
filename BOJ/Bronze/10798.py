# 10798

words = []

for _ in range(5):
  words.append(list(input()))

word = ''

for i in range(15):
  for j in range(5):
    try:
      word += words[j][i]
    except IndexError:
      continue
    
print(word)