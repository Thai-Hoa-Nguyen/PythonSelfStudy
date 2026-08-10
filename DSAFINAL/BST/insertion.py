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

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
    # we reach empty spot
        if node is None:
            return None
        
        #search left
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            #case 1
            if node.left is None and node.right is None:
                return None
            
            #case 2 only right child
            if node.left is None:
                return node.right

            #case 2
            if node.right is None:
                return node.left
            
            #case 3 2 children
            successor = self._find_min(node.right)

            node.value = successor.value

            node.right = self._remove(node.right, successor.value)

            return node

    def _find_min(self, node):
        while node.left:
            node = node.left
            
        return node