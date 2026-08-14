class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # =========================
    # INSERT
    # =========================

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)

        elif val > node.val:
            node.right = self._insert(node.right, val)

        return node

    # =========================
    # REMOVE
    # =========================

    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if node is None:
            return None

        if val < node.val:
            node.left = self._remove(node.left, val)

        elif val > node.val:
            node.right = self._remove(node.right, val)

        else:
            # Case 1: No children
            if node.left is None and node.right is None:
                return None

            # Case 2: Only right child
            if node.left is None:
                return node.right

            # Case 3: Only left child
            if node.right is None:
                return node.left

            # Case 4: Two children
            successor = self._find_min(node.right)

            node.val = successor.val

            node.right = self._remove(
                node.right,
                successor.val
            )

        return node

    # =========================
    # FIND MIN
    # =========================

    def _find_min(self, node):
        while node.left is not None:
            node = node.left

        return node

    # =========================
    # FIND SIBLING
    # =========================

    def find_sibling(self, target_val):
        if self.root is None:
            return None

        # Root has no sibling
        if self.root.val == target_val:
            return None

        current = self.root

        while current is not None:

            # Target is the left child
            if current.left is not None:
                if current.left.val == target_val:
                    return current.right

            # Target is the right child
            if current.right is not None:
                if current.right.val == target_val:
                    return current.left

            # Continue searching using BST property
            if target_val < current.val:
                current = current.left
            else:
                current = current.right

        # Target was not found
        return None

    # =========================
    # INORDER
    # Left -> Root -> Right
    # =========================

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.val, end=" ")
        self.inorder(node.right)

    # =========================
    # PREORDER
    # Root -> Left -> Right
    # =========================

    def preorder(self, node):
        if node is None:
            return

        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    # =========================
    # POSTORDER
    # Left -> Right -> Root
    # =========================

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=" ")

    # =========================
    # LEVEL ORDER / BFS
    # =========================

    def levelorder(self):
        if self.root is None:
            return

        queue = [self.root]
        index = 0

        while index < len(queue):
            current = queue[index]
            index += 1

            print(current.val, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)