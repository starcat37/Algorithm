# 5800

K = int(input())
for i in range(1, K+1):
  inputs = list(map(int, input().split()))
  N = inputs[0]
  grades = inputs[1:]
  grades.sort(reverse=True)
  gaps = [grades[i] - grades[i+1] for i in range(len(grades) - 1)]
  print("Class", i)
  print("Max", str(grades[0]) + ",", "Min", str(grades[-1]) + ",", "Largest gap", max(gaps))
