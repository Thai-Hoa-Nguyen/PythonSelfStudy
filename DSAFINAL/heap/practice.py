arr = []

def insert(val):
    arr.append(val)
    percolate_up(len(arr) - 1)

def parent(val):
    return (val - 1) // 2

def percolate_up(val):
    while val > 0 and arr[val] < arr[parent(val)]:
        parent_idx = parent(val)
        arr[val], arr[parent_idx] = arr[parent_idx], arr[val]
        val = parent_idx


#Test
insert(10)
insert(4)
insert(20)
insert(2)

print(arr)