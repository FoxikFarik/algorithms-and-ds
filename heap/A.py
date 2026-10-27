import sys

class maxHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0
    
    def siftUp(self, i):
        while(i // 2 > 0 and self.items[i] > self.items[i//2]):
                self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
                i = i//2
    
    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.siftUp(self.size)
        
    def extract(self):
        if self.size == 0:
            return None
        el = self.items[1]
        self.items[1] = self.items[self.size]
        self.size -= 1
        self.items.pop()
        self.siftDown(1)
        return el
    
    def indMaxChild(self, i):
        if i * 2 + 1 > self.size:
            return i*2
        if self.items[i*2] > self.items[i*2+1]:
            return i*2
        return i*2+1
    
    def siftDown(self, i):
        while i*2 <= self.size:
            j = self.indMaxChild(i)
            if self.items[i] < self.items[j]:
                self.items[i], self.items[j] = self.items[j], self.items[i]
            i = j
    

inputs = sys.stdin.read().split()
N = int(inputs[0])
pos = 1
heap = maxHeap()
for _ in range(N):
    cmd = inputs[pos]
    if cmd == '0':
        k = inputs[pos+1]
        heap.insert(int(k))
        pos += 1
    if cmd == '1':
        print(heap.extract())
    pos += 1
        