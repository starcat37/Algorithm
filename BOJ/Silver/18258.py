# 28278

# 앞 -- 뒤

from collections import deque
import sys
input = sys.stdin.readline

class Queue:
  def __init__(self):
    self.queue = deque()
    
  def push(self, X):
    self.queue.append(X)
    
  def pop(self):
    if len(self.queue):
      element = self.queue.popleft()
      print(element)
    else:
      print(-1)
  
  def size(self):
    print(len(self.queue))
  
  def empty(self):
    if len(self.queue):
      print(0)
    else:
      print(1)
      
  def front(self):
    if len(self.queue):
      print(self.queue[0])
    else:
      print(-1)
      
  def back(self):
    if len(self.queue):
      print(self.queue[-1])
    else:
      print(-1)
      
N = int(input())
MyQueue = Queue()
for _ in range(N):
  inst = input().rstrip()
  
  if inst.startswith("push"):
    push, X = inst.split()
    MyQueue.push(int(X))
  
  elif inst == "pop":
    MyQueue.pop()
    
  elif inst == "size":
    MyQueue.size()
    
  elif inst == "empty":
    MyQueue.empty()
    
  elif inst == "front":
    MyQueue.front()
    
  elif inst == "back":
    MyQueue.back()
  
  else:
    print("Undefined Instruction")
