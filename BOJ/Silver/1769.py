# 1769

X = int(input())
cnt = 0

def switch_question(X):
    return sum(map(int, list(str(X))))

while X >= 10:
    X = switch_question(X)
    cnt += 1

print(cnt)
print("NO" if X % 3 else "YES")