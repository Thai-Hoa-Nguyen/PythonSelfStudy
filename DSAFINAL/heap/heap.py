class MinHeap:
    def __init__(self):
        self.heap = []

    #formula
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def insert(self, value):
        self.heap.append(value)
        self.percolate_up(len(self.heap)-1)

    def percolate_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            parent_idx = self.parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

