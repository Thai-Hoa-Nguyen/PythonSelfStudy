class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value

            node.right = self._remove(node.right, successor.value)

            return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return

        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)

    def posorder(self, node):
        if node is None:
            return

        self.posorder(node.left)
        self.posorder(node.right)
        print(node.value)
 
    def levelorder(self):
        if self.root is None:
            return

        queue = [self.root]
        index = 0

        while index < len(queue):
            node = queue[index]
            index += 1

            print(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)