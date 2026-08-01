class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # ====================================
    # INSERT
    # ====================================

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self._insert(root.left, value)

        elif value > root.data:
            root.right = self._insert(root.right, value)

        return root

    # ====================================
    # SEARCH
    # ====================================

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):

        if root is None:
            return False

        if value == root.data:
            return True

        if value < root.data:
            return self._search(root.left, value)

        return self._search(root.right, value)

    # ====================================
    # PRE-ORDER
    # NODE → LEFT → RIGHT
    # ====================================

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):

        if root is None:
            return

        print(root.data)

        self._preorder(root.left)

        self._preorder(root.right)

    # ====================================
    # IN-ORDER
    # LEFT → NODE → RIGHT
    # ====================================

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):

        if root is None:
            return

        self._inorder(root.left)

        print(root.data)

        self._inorder(root.right)

    # ====================================
    # POST-ORDER
    # LEFT → RIGHT → NODE
    # ====================================

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):

        if root is None:
            return

        self._postorder(root.left)

        self._postorder(root.right)

        print(root.data)

    # ====================================
    # BREADTH-FIRST
    # ====================================

    def breadth_first(self):

        if self.root is None:
            return

        queue = []

        queue.append(self.root)

        while len(queue) > 0:

            current = queue.pop(0)

            print(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    # ====================================
    # FIND MIN
    # ====================================

    def find_min(self, root):

        while root.left is not None:
            root = root.left

        return root

    # ====================================
    # REMOVE
    # ====================================

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, root, value):

        if root is None:
            return None

        if value < root.data:
            root.left = self._remove(root.left, value)

        elif value > root.data:
            root.right = self._remove(root.right, value)

        else:

            # No children
            if root.left is None and root.right is None:
                return None

            # Only right child
            if root.left is None:
                return root.right

            # Only left child
            if root.right is None:
                return root.left

            # Two children
            successor = self.find_min(root.right)

            root.data = successor.data

            root.right = self._remove(
                root.right,
                successor.data
            )

        return root

tree = BST()

tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Pre-order:")
tree.preorder()

print("\nIn-order:")
tree.inorder()

print("\nPost-order:")
tree.postorder()

print("\nBreadth-first:")
tree.breadth_first()