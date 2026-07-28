class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _parent(self, i):
        return (i - 1) // 2

    def _percolate_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            parent_idx = self._parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

heap = MinHeap()
for num in [15, 10, 20, 5, 8]:
    heap.insert(num)

print(heap.heap)