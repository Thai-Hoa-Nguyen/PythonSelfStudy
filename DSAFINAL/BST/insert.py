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

    # Remove a node
    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        # Value wasn't found
        if node is None:
            return None

        # Search left
        if value < node.value:
            node.left = self._remove(node.left, value)

        # Search right
        elif value > node.value:
            node.right = self._remove(node.right, value)

        # Found the node
        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None

            # Case 2: only right child
            if node.left is None:
                return node.right

            # Case 2: only left child
            if node.right is None:
                return node.left

            # Case 3: two children
            successor = self._find_min(node.right)

            node.value = successor.value

            node.right = self._remove(
                node.right,
                successor.value
            )

        return node

    # Helper function
    def _find_min(self, node):
        while node.left is not None:
            node = node.left

        return node


# Create BST
bst = BST()

# Insert values
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

# Traversals
print("Inorder:")
bst.inorder(bst.root)

print("\nPreorder:")
bst.preorder(bst.root)

print("\nPostorder:")
bst.postorder(bst.root)