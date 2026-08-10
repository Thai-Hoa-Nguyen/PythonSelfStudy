class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
         
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        return node

    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return
        
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def posorder(self, node):
        if node is None:
            return
        
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.data)

arr = BST()
for data in [5,7,6,3,4,9,1,2,3]:
    arr.insert(data)
print("inorder")
arr.inorder(arr.root)
print("preorder")
arr.preorder(arr.root)