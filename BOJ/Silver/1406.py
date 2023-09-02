# 1406
# 시간초과
# 큐...

text = "." + (".").join(input()) + "."
M = int(input())
cursor = len(text) - 1
for _ in range(M):
  command = input()
  if command == "L":
    if cursor != 0:
      cursor -= 2
  if command == "D":
    if cursor != len(text) - 1:
      cursor += 2
  if command == "B":
    if cursor != 0:
      text = text[:cursor-2] + text[cursor:]
      cursor -= 2
  if command.startswith("P"):
    P, string = command.split()
    string = "." + (".").join(string)
    text = text[:cursor] + string + text[cursor:]
    cursor += 2
    
print(text.replace(".", ""))