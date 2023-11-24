# 1717
# 유니언 파인드

# find 연산 - 대표 노드를 찾는 연산
def find(a):
  if a == catalog[a]: # catalog index = catalog 값 -> 본인이 대표 노드임
    return a
  else:
    catalog[a] = find(catalog[a]) # 재귀 형태로 반복
    return catalog[a] # 리턴까지 해주기...

# union 연산
def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    catalog[b] = a # b의 대표 노드값을 a의 대표 노드값으로 변경

# 두 원소가 같은 집합에 있는지 확인
def check(a, b):
  a = find(a)
  b = find(b)
  return True if a == b else False # catalog[a]가 항상 대표 노드인 것이 아니므로 꼭 find로 찾아야 함

# 입력받기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

catalog = [i for i in range(n+1)]

for _ in range(m):
  inst, a, b = map(int, input().split())
  if inst == 0:
    union(a, b)
  else:
    print("YES") if check(a, b) else print("NO")
