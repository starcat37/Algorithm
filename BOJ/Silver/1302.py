# 1302

N = int(input())
books = []
for _ in range(N):
  books.append(input())
  
print(sorted(books, reverse=True, key=lambda x: (-books.count(x), x))[-1])