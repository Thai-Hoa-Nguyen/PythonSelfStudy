```
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
        elif node.right is None:
            return node.left
        
        successor = self._find_min(node.right)
        node.value = successor.value
        node.right = self._remove(node.right, successor.value)

def _find_min(self, node):
    while node.left:
        node = node.left
    return node
```