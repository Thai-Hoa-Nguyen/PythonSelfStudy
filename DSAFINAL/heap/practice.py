class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        self.percolate_up(len(self.arr) - 1)

    def parent(self, val):
        return (val - 1) // 2
        
    def percolate_up(self, index):
        while index > 0:


  
heap = MinHeap()

for num in [15,10]:
    heap.insert(num)

print(heap.arr)