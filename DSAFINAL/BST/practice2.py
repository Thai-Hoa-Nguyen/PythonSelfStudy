class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def __insert(self, current, data):
        if current is None:
            return Node(data)

        if data < current.data:
            current.left = self.__insert(current.left, data)
        elif data > current.data:
            current.right = self.__insert(current.right, data)

        return current

    def display(self, current):
        print(current.data)

arr = BST()
arr.insert(4)
arr.insert(3)
arr.insert(2)

arr.display(arr)

