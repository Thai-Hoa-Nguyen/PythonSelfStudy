class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion - Recursive
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    # Inorder: LEFT -> ROOT -> RIGHT
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    # Preorder: ROOT -> LEFT -> RIGHT
    def preorder(self, node):
        if node is None:
            return

        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)

    # Postorder: LEFT -> RIGHT -> ROOT
    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)

bst = BST()

for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("Inorder:")
bst.inorder(bst.root)

print("Preorder:")
bst.preorder(bst.root)

print("Postorder:")
bst.postorder(bst.root)