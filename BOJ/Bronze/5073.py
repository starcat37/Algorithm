# 5073

while True:
  lengths = list(map(int, input().split()))
  if sum(lengths) == 0: break
  
  if lengths[0] + lengths[1] > lengths[2] and lengths[1] + lengths[2] > lengths[0] and lengths[2] + lengths[0] > lengths[1]:
    types = set(lengths)
    if len(types) == 1: print("Equilateral")
    elif len(types) == 2: print("Isosceles")
    else: print("Scalene")
  else:
    print("Invalid") 
