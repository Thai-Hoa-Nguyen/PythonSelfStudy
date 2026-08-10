class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    #Insertion Recursive
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

    #Traversal [BFS] [recursive]
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def posorder(self, node):
        if node is None:
            return

        self.posorder(node.left)
        self.posorder(node.right)
        print(node.data)

    def preorder(self, node):
        if node is None:
            return

        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)