class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
     
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return "error"
        self.size -= 1
        return self.stack.pop(-1)
        
    def top(self):
        if self.size == 0:
            return "error"
        return self.stack[-1]
    
    def clear(self):
        self.stack = []
        self.size = 0

brackets = Stack()
line = input()
result = True
for el in line:
    if el in '([{':
        brackets.push(el)
    elif el in ')]}' and brackets.is_empty():
        result = False
        break
    elif (el == ')' and brackets.top() == '(') or \
         (el == ']' and brackets.top() == '[') or \
         (el == '}' and brackets.top() == '{'):
        brackets.pop()
    else:
        result = False
        break
if result and brackets.is_empty():
    print('yes')
else:
    print('no')