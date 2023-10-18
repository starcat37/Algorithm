# 28278

import sys
input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self, X):
    self.stack.append(X)
    
  def pop(self):
    return -1 if Stack.empty(self) else self.stack.pop()
    
  def length(self):
    length = len(self.stack)
    return length
    
  def empty(self):
    return int(not bool(Stack.length(self)))
    
  def head(self):
    return -1 if Stack.empty(self) else self.stack[-1]
  
N = int(input().rstrip())
MyStack = Stack()
for _ in range(N):
  inst = input().rstrip()
  inst_flag = int(inst[0])
  if inst_flag == 1:
    MyStack.push(int(inst.split()[-1]))
  elif inst_flag == 2:
    result = MyStack.pop()
    print(result)
  elif inst_flag == 3:
    result = MyStack.length()
    print(result)
  elif inst_flag == 4:
    result = MyStack.empty()
    print(result)
  elif inst_flag == 5:
    result = MyStack.head()
    print(result)
  else:
    print("Not Defined")