# 2386

while True:
  query = input()
  if query == "#": break
  ch, sen = query[0], query[2:].lower()
  print(ch, sen.count(ch))
