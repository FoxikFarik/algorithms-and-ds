class minStack:
    def __init__(self):
            self.stack = []
            self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, item):
        if self.size == 0:
            self.stack.append([item, item])
        else:
            self.stack.append([item, min(item, self.stack[-1][1])])
        self.size += 1
    
    def pop(self):
        self.size -= 1
        return self.stack.pop(-1)
        
    def back(self):
        return self.stack[-1][0]
    
    def getMin(self):
        if self.size > 0:
            return self.stack[-1][1]
        return None
    

class minQueue:
    def __init__(self):
        self.left = minStack()
        self.right = minStack()
        
    def size(self):
        return self.left.size + self.right.size
    
    def push(self, item):
        self.right.push(item)
    
    def getMin(self):
        m1 = self.left.getMin()
        m2 = self.right.getMin()
        if m1 is not None and m2 is not None:
            return min(m1, m2)
        return m1 if m1 is not None else m2
     
    def pop(self):
        if self.left.is_empty():
            while self.right.size > 0:
                self.left.push(self.right.pop()[0])
                
        return self.left.pop()

n, k = map(int, input().split())
items = list(map(int, input().split()))
window = minQueue()
for i in range(k-1):
    window.push(items[i])
    
for i in range(k-1, n):
    window.push(items[i])
    print(window.getMin())
    window.pop()

