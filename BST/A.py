import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def search(self, key):
        return self._search(self.root, key)
        
    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
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

    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node
    
    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def print_tree(self, node, level):
        if node is None:
            return;
        self.print_tree(node.left, level+1)
        for i in range(level):
            print('.', end='')
        print(node.data)
        self.print_tree(node.right, level+1)
    
BST = BinarySearchTree()
for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0].upper()
        if command == "PRINTTREE":
            BST.print_tree(BST.root, 0)
        elif command == "ADD":
            n = int(parts[1])
            if not BST.search(n):
                BST.insert(n)
                print("DONE")
            else:
                print("ALREADY")
        elif command == "DELETE":
            n = int(parts[1])
            if BST.search(n):
                BST.delete(n)
                print("DONE")
            else:
                print("CANNOT")
        elif command == "SEARCH":
            n = int(parts[1])
            if BST.search(n):
                print("YES")
            else:
                print("NO")