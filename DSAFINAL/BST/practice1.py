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

    def _insert(self, current, data):

        if current is None:
            return Node(data)

        if data < current.data:
            current.left = self._insert(current.left, data)
        elif data > current.data:
            current.right = self._insert(current.right, data)

        return current

    def inorder(self, current):
        if current is None:
            return

        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

tree = BST()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

tree.inorder(tree.root)
