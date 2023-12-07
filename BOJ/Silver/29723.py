# 29723

N, M, K = map(int, input().split())

grades = {}

for _ in range(N):
  course, score = input().split()
  score = int(score)
  grades[course] = score

result = 0

for _ in range(K):
  course = input()
  result += grades[course]
  del grades[course]
  M -= 1
  
min_result = result + sum(sorted(grades.values())[:M])
max_result = result + sum(sorted(grades.values())[len(grades.values())-M:])

print(min_result, max_result)
