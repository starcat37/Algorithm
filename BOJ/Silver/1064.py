# 1064** -> 평행사변형의 성립 조건, 기하학 공식 필요

import math

x1, y1, x2, y2, x3, y3 = map(int, input().split(" "))

AB = math.dist([x1, y1], [x2, y2])
BC = math.dist([x2, y2], [x3, y3])
CA = math.dist([x3, y3], [x1, y1])

if (x3 - x2)*(y2 - y1) == (x2 - x1) * (y3 - y2):
    print('-1.0')
else:
    lengths = [AB + BC, BC + CA, CA + AB]
    print(2 * (max(lengths) - min(lengths)))