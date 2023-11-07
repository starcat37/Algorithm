# 11005

import string

N, B = map(int, input().split())

def convert(num, base):
  number = string.digits + string.ascii_uppercase
  q, r = divmod(num, base)
  return convert(q, base) + number[r] if q else number[r]

print(convert(N, B))
