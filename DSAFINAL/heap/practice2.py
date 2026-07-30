# Max Heap insertion and percolate up
#Max Heap without class
# Insertion
#     |
# Percolate-up
arr = []

def insert(val):
    arr.append(val)
    percolate_idx = len(arr) - 1
    percolate_up(percolate_idx)

def find_parent(val):
    return (val - 1) // 2

def percolate_up(val):
    #different between max heap and min heap insertion is this one
    #whenever      -> arr[val] > arr[find_parent(val)]: if it > is max and otherwise
    while val > 0 and arr[val] > arr[find_parent(val)]:
        parent_idx = find_parent(val)
        arr[val], arr[parent_idx] = arr[parent_idx], arr[val]
        val = parent_idx
        

insert(4)
insert(10)
insert(8)
insert(2)
insert(20)
insert(21)

print(arr)