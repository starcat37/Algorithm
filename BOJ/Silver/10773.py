#10773

K = int(input())

acc_book = []

for _ in range(K):
    num = int(input())
    if num == 0:
        acc_book.pop()
    else:
        acc_book.append(num)

print(sum(acc_book))