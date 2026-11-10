import queue
import sys

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
    
    
BST = BinarySearchTree()
inputs = sys.stdin.read().split()
N = int(inputs[0])
pos = 1
last_command = ''
last_result = 0
for _ in range(N):
    cmd = inputs[pos]
    if cmd == '?':
        key = int(inputs[pos+1])
        closest = -1
        node = BST.root
        while node:
            if node.data >= key:
                closest = node.data
                node = node.left
            else:
                node = node.right
        print(closest)
        last_command = '?'
        last_result = closest
        pos += 2
    elif cmd == '+':
        if last_command == '?':
            BST.insert((int(inputs[pos+1]) + last_result) % 10 ** 9)
        else:
            BST.insert(int(inputs[pos+1]))
        last_command = '+'
        pos += 2