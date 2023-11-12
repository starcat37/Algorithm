# 9063

N = int(input())
x_coordinates = []
y_coordinates = []

for _ in range(N):
  x, y = map(int, input().split())
  x_coordinates.append(x)
  y_coordinates.append(y)
  
x_coordinates.sort()
y_coordinates.sort()

print((x_coordinates[-1] - x_coordinates[0]) * (y_coordinates[-1] - y_coordinates[0]))
