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
        node.right = self._remove(self.right, successor.value)

def _find_min(self, node):
    while node.left:
        node = node.left
    return node

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

def inorder(self, node):
    if node is None:
        return
        
    self.inorder(node.left)
    print(node.value)
    self.inorder(node.right)

def posorder(self, node):
    if node is None:
        return
    
    self.posorder(node.left)
    self.posorder(node.right)
    print(node.value)

def preorder(self, node):
    if node is None:
        return
    
    print(node.value)
    self.preorder(node.left)
    self.preorder(node.right)