from sys import stdin

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return "error"
        self.size -= 1
        return self.stack.pop()
        
    def back(self):
        if self.size == 0:
            return "error"
        return self.stack[-1]
    
    def clear(self):
        self.stack.clear()
        self.size = 0
        
    
stack = Stack()
commands = stdin.readlines()
for line in commands:
    cmd = line.rstrip()
    if " " in cmd:
        cmd, argument = cmd.split()
    if cmd == "push":
        stack.push(int(argument))
        print("ok")
    elif cmd == "pop":
        print(stack.pop())
    elif cmd == "back":
        print(stack.back())
    elif cmd == "size":
        print(stack.size)
    elif cmd == "clear":
        stack.clear()
        print('ok')
    elif cmd == "exit":
        print("bye")
        break