# 16430

import math

A, B = map(int, input().split())

P = B - A
Q = B

gcd = math.gcd(P, Q)
P //= gcd
Q //= gcd
print(P, Q)