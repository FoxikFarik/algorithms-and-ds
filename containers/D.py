from sys import stdin

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def back(self):
        return self.stack[-1]
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def clear(self):
        self.stack.clear()
        self.size = 0

class Queue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()
    
    def size(self):
        return self.left.size + self.right.size
    
    def is_empty(self):
        return self.left.is_empty() and self.right.is_empty()
    
    def push(self, item):
        self.right.push(item)
    
    def balance(self):
        for i in range(self.right.size):
            self.left.push(self.right.pop())
            
    def front(self):
        if self.is_empty():
            return "error"
        if self.left.size == 0:
            self.balance()
        return self.left.back()
    
    def pop(self):
        if self.is_empty():
                return "error"
        if self.left.size == 0:
            self.balance()
        return self.left.pop()
    
    def clear(self):
        self.left.clear()
        self.right.clear()
        
    
queue = Queue()
commands = stdin.readlines()
for line in commands:
    cmd = line.rstrip()
    if " " in cmd:
        cmd, argument = cmd.split()
    if cmd == "push":
        queue.push(int(argument))
        print("ok")
    elif cmd == "pop":
        print(queue.pop())
    elif cmd == "front":
        print(queue.front())
    elif cmd == "size":
        print(queue.size())
    elif cmd == "clear":
        queue.clear()
        print('ok')
    elif cmd == "exit":
        print("bye")
        break