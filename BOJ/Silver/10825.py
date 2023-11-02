# 10825

N = int(input())
class_scores = []
for _ in range(N):
  name, kor, mat, eng = map(str, input().split())
  class_scores.append(tuple([name, int(kor), int(mat), int(eng)]))

sorted_class_scores = sorted(class_scores, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
  print(sorted_class_scores[i][0])
