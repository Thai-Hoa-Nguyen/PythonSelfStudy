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
        
def remove():

    if len(arr) == 0:
        return None

    minimum = arr[0]

    # Move last element to the root
    arr[0] = arr[-1]

    # Remove last element
    arr.pop()

    # Restore heap
    if len(arr) > 0:
        percolate_down(0)

    return minimum


def percolate_down(index):

    while True:

        left = 2 * index + 1
        right = 2 * index + 2

        smallest = index

        # Compare left child
        if left < len(arr) and arr[left] < arr[smallest]:
            smallest = left

        # Compare right child
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right

        # Heap property satisfied
        if smallest == index:
            break

        # Swap
        arr[index], arr[smallest] = arr[smallest], arr[index]

        # Continue downward
        index = smallest


arr = [5, 10, 15, 20, 30, 40]

removed = remove()

print("Removed:", removed)
print("Heap:", arr)