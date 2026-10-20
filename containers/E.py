from sys import stdin

class Deque:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def clear(self):
        self.items.clear()
        
    def push_front(self, item):
        self.items = [item] + self.items
    
    def push_back(self, item):
        self.items.append(item)
    
    def pop_front(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)
    
    def pop_back(self):
        if self.is_empty():
            return "error"
        return self.items.pop()
    
    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]
    
    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]


deque = Deque()
commands = stdin.readlines()
for line in commands:
    cmd = line.rstrip()
    if " " in cmd:
        cmd, argument = cmd.split()
    if cmd == "push_front":
        deque.push_front(int(argument))
        print("ok")
    elif cmd == "push_back":
        deque.push_back(int(argument))
        print("ok")
    elif cmd == "pop_front":
        print(deque.pop_front())
    elif cmd == "pop_back":
        print(deque.pop_back())
    elif cmd == "front":
        print(deque.front())
    elif cmd == "back":
        print(deque.back())
    elif cmd == "size":
        print(deque.size())
    elif cmd == "clear":
        deque.clear()
        print('ok')
    elif cmd == "exit":
        print("bye")
        break