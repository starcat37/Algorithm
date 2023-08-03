# 7568** - chatgpt
# 너무 복잡하게 푼 것 같음...
# 문제 표현에 집중하기...

N = int(input())
people = []

for i in range(N):
    weight, height = map(int, input().split(" "))
    people.append([weight, height, i])

for i in range(N):
    cnt = 1
    for j in range(N):
        if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
            cnt += 1
    print(cnt, end=" ")

# sort_result = sorted(people, reverse=True, key=lambda x: (x[0], x[1]))
# cnt = 1

# for i in range(N):
#     if i == N-1:
#         if sort_result[i][0] < sort_result[i-1][0] and sort_result[i][1] < sort_result[i-1][1]:
#             cnt += 1
#             sort_result[i].append(cnt)
#         else:
#             sort_result[i].append(cnt)
#     else:
#         if sort_result[i][0] > sort_result[i+1][0] and sort_result[i][1] > sort_result[i+1][1]:
#             sort_result[i].append(cnt)
#             cnt += 1
#         else:
#             sort_result[i].append(cnt)
            
# people_result = sorted(sort_result, key=lambda x: x[2])
# print(" ".join(list(map(str, [i[3] for i in people_result]))))

# N = int(input())
# catalog = []

# for _ in range(N):
#     weight, height = map(int, input().split(" "))
#     catalog.append([weight, height])
    
# sortResult = sorted(catalog, reverse=True, key=lambda x: (x[0], x[1]))

# cnt = 1
# sizeResult = []
# for i in range(N):
#     if i == N-1:
#         if sortResult[i][0] < sortResult[i-1][0] and sortResult[i][1] < sortResult[i-1][1]:
#             cnt += 2
#             sizeResult.append(cnt) 
#         else:
#             cnt += 1
#             sizeResult.append(cnt) 
#     else:
#         if sortResult[i][0] > sortResult[i+1][0] and sortResult[i][1] > sortResult[i+1][1]:
#             sizeResult.append(cnt)
#             cnt += 1
#         else:
#             sizeResult.append(cnt)

# result = []
# for person in catalog:
#     result.append(sizeResult[sortResult.index(person)])
    
# print(" ".join(list(map(str, result))))