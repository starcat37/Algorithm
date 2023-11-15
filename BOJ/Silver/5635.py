# 5635

N = int(input())

people = dict()

for _ in range(N):
  name, day, month, year = map(str, input().split())
  people[name] = [int(year), int(month), int(day)]
  
sorted_people = sorted(people.items(), reverse=True, key = lambda item: (item[1][0], item[1][1], item[1][2]))

print(sorted_people[0][0])
print(sorted_people[-1][0])
