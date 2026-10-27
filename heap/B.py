class minHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0
    
    def siftUp(self, i):
        while(i // 2 > 0 and self.items[i] < self.items[i//2]):
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
    
    def indMinChild(self, i):
        if i * 2 + 1 > self.size:
            return i*2
        if self.items[i*2] < self.items[i*2+1]:
            return i*2
        return i*2+1
    
    def siftDown(self, i):
        while i*2 <= self.size:
            j = self.indMinChild(i)
            if self.items[i] > self.items[j]:
                self.items[i], self.items[j] = self.items[j], self.items[i]
            i = j
            

N = int(input())
arr = list(map(int, input().split()))
heap = minHeap()
for el in arr:
    heap.insert(el)

for i in range(N):
    print(heap.extract(), end=" ")