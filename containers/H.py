import sys
from collections import deque

def balance(left: deque, right: deque):
    if(len(left) > len(right) + 1):
        right.appendleft(left.pop())
    elif(len(left) < len(right)):
        left.append(right.popleft())


left = deque()
right = deque()

inputs = sys.stdin.read().split()
N = int(inputs[0])
pos = 1
for _ in range(N):
    cmd = inputs[pos]
    if cmd == '+':
        right.append(inputs[pos+1])
        pos += 2
    elif cmd == '*':
        left.append(inputs[pos+1])
        pos += 2
    else:
        print(left.popleft())
        pos += 1
    balance(left, right)
