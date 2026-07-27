# Data Structures & Algorithms: Heaps & Trees Review

## 1. What is a Heap?

A **Heap** is a specialized **complete binary tree** stored in an **array** and commonly used to implement a **Priority Queue**.

A heap maintains a **heap-order property**:
* **Min-Heap:** Every parent is **less than or equal to** its children.
* **Max-Heap:** Every parent is **greater than or equal to** its children.

### Time Complexities
* **Access Min/Max:** $O(1)$
* **Insertion:** $O(\log n)$
* **Extract Min/Max:** $O(\log n)$

> **Two Essential Rules:**
> 1. **Completeness (Structural Rule)**
> 2. **Heap Order (Value Rule)**

---

## 2. Completeness (Structural Rule)

A binary tree is **complete** if:
1. Every level, except possibly the last, is completely filled.
2. The last level is filled **from left to right** without any gaps.

```text
       ✅ VALID COMPLETE TREE          ❌ INVALID (NOT COMPLETE)

               (10)                           (10)
              /    \                         /    \
           (20)    (30)                   (20)    (30)
           /  \    /                      /  \       \
        (40)(50)(60)                  (40)(50)     (70)
                                                  ^
                                          Missing left child
                                              of (30)

```

### Why Completeness Matters

* Keeps tree height bounded at **$O(\log n)$**.
* Enables efficient storage in a **1D array** without wasting space.
* Allows child/parent navigation using fast index calculations.

---

## 3. Heap Order (Value Rule)

### Min-Heap

* **Rule:** $\text{Parent} \le \text{Children}$
* Smallest element is at the root.
* All ancestors are $\le$ their descendants.

### Max-Heap

* **Rule:** $\text{Parent} \ge \text{Children}$
* Largest element is at the root.
* All ancestors are $\ge$ their descendants.

```text
         MIN-HEAP                      MAX-HEAP

            (5)                          (90)
           /   \                        /    \
        (12)  (15)                   (70)   (80)
        /  \                         /  \
     (20)(25)                     (30)(40)

```

> **Note:** Sibling nodes have no ordering requirement relative to each other.

---

## 4. Summary Table

| Property | Rule | Purpose |
| --- | --- | --- |
| **Completeness** | All levels full except last (filled left-to-right). | Maintains $O(\log n)$ height and efficient array layout. |
| **Heap Order** | **Min:** Parent $\le$ Children <br>

<br> **Max:** Parent $\ge$ Children | Guarantees $O(1)$ access to min or max element. |

---

## 5. Underlying Data Structure & Array Representation

The underlying data structure of a Heap is a **1D Array (dynamic List in Python)**.

Because the tree is strictly complete, parent-child positions map directly via index arithmetic ($O(1)$ calculation):

For an element at index $i$ (0-indexed):

* **Left Child:** `2 * i + 1`
* **Right Child:** `2 * i + 2`
* **Parent:** `(i - 1) // 2`

```text
Tree View:               Array Representation:
       (10) [0]           Index:  0   1   2   3   4
      /        \          Value: [10, 15, 30, 40, 50]
   (15) [1]   (30) [2]           |   |   |   |   |
   /    \                        |   +---+---+   +-- Left child of 15 is at index 3
(40)[3] (50)[4]                  +-------+------ Right child of 10 is at index 2

```

**Why use an array?**

* Zero memory overhead (no node pointers required).
* Superior CPU cache locality.
* Instant index calculations.

---

## 6. Heap Operations

### A. Insertion (`percolate_up`)

1. **Append to End:** Place new element at the bottom-leftmost open spot (maintains Completeness).
2. **Compare with Parent:** Check if heap order is violated using `parent_idx = (i - 1) // 2`.
3. **Swap & Repeat:** Swap upward until node is in proper order or reaches root.

```text
1. Append 5 at end:               2. Percolate Up (Swap 5 & 18):     3. Final Min-Heap:
          (10)                                (10)                              (5)
         /    \                              /    \                            /   \
      (18)    (30)                        (5)     (30)                      (10)   (30)
      /                                   /                                 /
    (5)  <-- appended                   (18)                              (18)

```

* **Time Complexity:** $O(\log n)$

### B. Removal (`percolate_down`)

1. **Replace Root:** Overwrite root with the last leaf element, then pop the last element.
2. **Identify Target Child:** Compare root with children and find the smallest (Min-Heap) or largest (Max-Heap) child.
3. **Swap & Repeat:** Sift down until heap order is restored.

```text
1. Replace 5 with last leaf (18):   2. Percolate Down (Swap 18 & 10):   3. Final Min-Heap:
          (18)                              (10)                                (10)
         /    \                            /    \                              /    \
      (10)    (30)                      (18)    (30)                        (18)    (30)

```

* **Time Complexity:** $O(\log n)$

---

## 7. Python Object Implementations

### Min-Heap Class

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left_child(self, i): return 2 * i + 1
    def _right_child(self, i): return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            parent_idx = self._parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_val

    def _percolate_down(self, i):
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._percolate_down(smallest)

```

### Max-Heap Class

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left_child(self, i): return 2 * i + 1
    def _right_child(self, i): return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            parent_idx = self._parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

    def remove_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_val

    def _percolate_down(self, i):
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)
        size = len(self.heap)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._percolate_down(largest)

```

---

## 8. In-Place `heapify()` & `makeheap()`

| Feature | Min-Heap `heapify` | Max-Heap `heapify` |
| --- | --- | --- |
| **Goal** | Move smallest value up | Move largest value up |
| **Target Child** | Find **SMALLEST** child | Find **LARGEST** child |
| **Swap Condition** | Swap if parent $>$ smallest child | Swap if parent $<$ largest child |

### Python In-Place Functions

```python
def min_heapify(arr, n, i):
    smallest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def max_heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def makeheap(arr, heap_type="min"):
    n = len(arr)
    # Start at the last non-leaf parent node
    for i in range((n // 2) - 1, -1, -1):
        if heap_type == "min":
            min_heapify(arr, n, i)
        else:
            max_heapify(arr, n, i)

```

---

## 9. Heapsort

Heapsort transforms an unsorted array into a **Max-Heap**, repeatedly swaps the maximum element (root) with the end of the array, and shrinks the active heap boundary.

```python
def heapsort(arr):
    n = len(arr)

    # 1. Build Max-Heap in-place - O(n)
    for i in range((n // 2) - 1, -1, -1):
        max_heapify(arr, n, i)

    # 2. Extract elements back-to-front - O(n log n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move root to sorted end
        max_heapify(arr, i, 0)          # Restore heap on reduced size

    return arr

```

### Complexity & Characteristics

| Metric | Complexity |
| --- | --- |
| **Best / Avg / Worst Time** | $O(n \log n)$ |
| **Space Complexity** | **$O(1)$ (In-Place)** |
| **Stability** | **Not Stable** |

---

## 10. Binary Tree Fundamentals

### Core Terms

* **Root:** Topmost node (no parent).
* **Leaf:** Node with zero children.
* **Sibling:** Nodes sharing the same parent.
* **Internal Node:** Node with at least one child.

### Height vs. Depth

| Metric | Definition | Base Value |
| --- | --- | --- |
| **Depth** | Number of edges from **root** down to node. | Root depth = `0` |
| **Height** | Number of edges on **longest path** from node down to a leaf. | Leaf height = `0` |

### Structural Types

* **Full:** Nodes have either 0 or 2 children.
* **Complete:** All levels filled except last (filled left-to-right).
* **Perfect:** All internal nodes have 2 children; all leaves at same level.

### Traversals

* **Pre-order (Root $\rightarrow$ Left $\rightarrow$ Right):** Copying/cloning trees.
* **In-order (Left $\rightarrow$ Root $\rightarrow$ Right):** Sorted output on Binary Search Trees (BST).
* **Post-order (Left $\rightarrow$ Right $\rightarrow$ Root):** Bottom-up cleanup / directory size calculation.
* **Level-order (BFS):** Level-by-level processing; matches array heap index layout.