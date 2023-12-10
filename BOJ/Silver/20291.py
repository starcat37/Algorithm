# 20291

extensions = {}

N = int(input())
for _ in range(N):
  extension = input().split(".")[1]
  if extension in extensions:
    extensions[extension] += 1
  else:
    extensions[extension] = 1
    
for key, value in sorted(extensions.items()):
  print(key, value)
