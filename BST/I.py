class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node
    
    def balanced(self):
        return self._balanced(self.root)
    
    def _balanced(self, node):
        if node is None:
            return 0, True
        
        lHeight, lBalanced = self._balanced(node.left)
        rHeight, rBalanced = self._balanced(node.right)
        
        balanced = lBalanced and rBalanced and abs(rHeight - lHeight) <= 1
        
        height = 1 + max(lHeight, rHeight)
        return height, balanced

BST = BinarySearchTree()
row = input().split()
for el in row:
    if el != '0':
        BST.insert(int(el))

print("YES" if BST.balanced()[1] else "NO")
    
