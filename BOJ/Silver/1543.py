# 1543

import re
import sys
input = sys.stdin.readline

document = input().rstrip()
target = input().rstrip()

result = re.findall(target, document)

print(len(result))
