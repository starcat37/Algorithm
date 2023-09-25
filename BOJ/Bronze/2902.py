# 2902

import re

memo = input()
print(memo[0] + "".join(re.findall(r"-(.)", memo)))