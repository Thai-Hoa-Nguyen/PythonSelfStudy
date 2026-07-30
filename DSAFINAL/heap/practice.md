
# Exercise 1: Trace by Hand ⭐ (Warm-up)
Start with an empty heap.
Insert these numbers one by one:
```text
15, 10, 20, 5, 8
```
After **each insertion**, write the array representation of the heap.
Example format:
```text
arr = [5,8,20,15,10]
```
---

# Exercise 2: Implement `peek()` ⭐
Add a method that returns the smallest value without removing it.
Expected:
```python
    

heap = MinHeap()

for num in [15, 10, 20, 5, 8]:
    heap.insert(num)

print(heap.peek())
```
Output:

```text
5
```

---

# Exercise 3: Count Swaps ⭐⭐

Modify `percolate_up()` to count how many swaps occur during an insertion.

Example:

```python
heap.insert(5)
```

Output:

```text
Swaps: 2
```

---

# Exercise 4: Is It a Valid Heap? ⭐⭐

Write:

```python
def is_min_heap(heap):
```

It should return `True` if every parent is less than or equal to its children.

Example:

```python
is_min_heap([5, 8, 20, 15, 10])
```

Returns:

```text
True
```

Example:

```python
is_min_heap([10, 5, 20])
```

Returns:

```text
False
```

---

# Exercise 5: Build a Heap ⭐⭐⭐

Given:

```python
nums = [9, 7, 5, 12, 2, 1]
```

Insert them one at a time into your heap.

Print the heap after every insertion.

Example:

```text
After inserting 9:
[9]

After inserting 7:
[7, 9]

...
```

---

# Exercise 6: Visualize the Tree ⭐⭐⭐

After inserting:

```text
15, 10, 20, 5, 8, 30, 2
```

Draw the tree.

Example format:

```text
        2
      /   \
     8     5
    / \   / \
   ...
```

Then explain why every parent satisfies the min-heap property.

---

# Challenge ⭐⭐⭐⭐

Without running Python, determine the final heap after inserting:

```text
30
15
50
10
40
5
20
35
```

Write the final array.

---

## Recommended learning path

1. ✅ Insert
2. ✅ Parent index
3. ✅ Percolate up
4. ✅ Trace insertions by hand
5. ✅ Validate a heap
6. ➜ Next: **Remove minimum**
7. ➜ Learn **Percolate down**
8. ➜ Implement `heapify()`
9. ➜ Learn **Heap Sort**
