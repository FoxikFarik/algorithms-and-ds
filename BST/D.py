class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, key):
        self.size += 1
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def order_up(self):
        return self._order_up(self.root)
    
    def _order_up(self, node):
        if node is None:
            return []
        return self._order_up(node.left) + [node.data] + self._order_up(node.right)
    
    def order_down(self):
            return self._order_down(self.root)
        
    def _order_down(self, node):
        if node is None:
            return []
        return self._order_down(node.right) + [node.data] + self._order_down(node.left)
    
        

BST = BinarySearchTree()
row = input().split()
for el in row:
    if el != '0':
        BST.insert(int(el))

print(BST.order_down()[1])
    
