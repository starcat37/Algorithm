#4949

import re
import sys

def isBalanced(line):
    stack = "".join(re.findall(r"[()[\]]", line))
    if len(stack) == 0:
        print("yes")
    else:
        while (True):
            latest_stack = stack
            stack = re.sub(r"\(\)|\[\]", "", stack)
            if len(stack) == 0:
                print("yes")
                break
            elif latest_stack == stack:
                print("no")
                break
            else: continue

while (True):
    line = sys.stdin.readline().strip('\n')
    if line == ".": 
        break
    else:
        isBalanced(line)