def percolate_up(heap, index):
    while index > 0:
        parent_index = (index - 1) // 2
        
        # If the element is smaller than its parent, swap them!
        if heap[index] < heap[parent_index]:
            heap[index], heap[parent_index] = heap[parent_index], heap[index]
            # Move our focus index up to the parent's position
            index = parent_index
        else:
            # Heap property is satisfied — no more swaps needed
            break

def insert(heap, value):
    # Step 1: Append the new node at the very end (bottom-leftmost open spot)
    heap.append(value)
    
    # Step 2: Pass its index to percolate_up to float it to the right position
    last_index = len(heap) - 1
    percolate_up(heap, last_index)

# --- Example Usage ---
min_heap = [10, 15, 20, 30, 40]
print("Before insertion:", min_heap)

# Insert a new small element (e.g., 5)
insert(min_heap, 5)

print("After insertion :", min_heap)
# Output will be: [5, 15, 10, 30, 40, 20]