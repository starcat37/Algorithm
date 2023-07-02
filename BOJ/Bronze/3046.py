# 3046

import sys

r1, s = sys.stdin.readline().strip().split(' ')

# s == (r1 + r2) / 2
# r2 = 2s - r1

print(int(s)*2 - int(r1))