from collections import deque

expression = list(map(str, input().split()))
stack = deque()
for el in expression:
    if el in '+-*':
        b, a = stack.pop(), stack.pop()
        if el == '+':
            stack.append(a+b)
        elif el == '-':
            stack.append(a-b)
        else:
            stack.append(a*b)
    else:
        stack.append(int(el))

print(stack.pop())