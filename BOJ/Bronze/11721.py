# 11721

import re

string = input()
result = re.findall(".{10}|.+", string)
for i in result:
  print(i)