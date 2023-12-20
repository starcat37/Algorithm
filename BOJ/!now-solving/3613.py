# 3613
# 반례,,, 너무 많음
# https://www.acmicpc.net/board/view/92676

import re

def isJava(variable):
  return bool(re.findall("[A-Z]", variable)) and variable[0].islower()

def isCpp(variable):
  return bool(re.findall("[_]", variable)) and not bool(re.findall("[A-Z]", variable)) and variable[-1] != "_" and variable[0] != "_"

variable = input()
new_variable = ""

if isJava(variable) and not isCpp(variable):
  for c in variable:
    if c.isupper():
      new_c = "_" + c.lower()
      new_variable += new_c
    else:
      new_variable += c
  print(new_variable)
elif isCpp(variable) and not isJava(variable):
  new_variable = re.sub(r"_([a-z])", lambda match: match.group(1).upper(), variable)
  print(new_variable)
else:
  print("Error!")
