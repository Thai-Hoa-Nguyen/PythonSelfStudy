arr = []

def insert(val):
    arr.append(val)
    percolate_up(len(arr) - 1)

def parent(val):
    return (val - 1) // 2

def percolate_up(val):
    while val > 0 and arr[val] > arr[parent(val)]:
        parent_idx = parent(val)
        arr[val], arr[parent(val)] = arr[parent(val)], arr[val]
        val = parent_idx

insert(5)
insert(10)
insert(2)
insert(12)

print(arr)