## Exam Review Questions

**1.** Given a relatively balanced binary search tree, why is the search() function O(log n)?


**2.** Explain why you need a max_heap (biggest is at root, parent > children) for heap sort that sorts an array in ascending order (small to big).

**3.** If you were to implement a reverse phone directory (You enter a phone number to find a person), what data structure would you use for the table?

**4.**  Can you binary search a sorted linked list? Explain why or why not.

**5.** Given the following declaration of a binary search tree:
```python
class BST:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BST's init function
	def __init__(self):
		self.root = None
```
Write the following method:

```python
def print_between(self, min, max): 
```
This function prints every value in the tree that is between min and max inclusive. 
Function only visits a subtree where the values may be valid.

**6.** Given the following declaration of a binary tree:
```python
class BT:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BT's init function
	def __init__(self):
		self.root = None
```
Write the BT class method:
```python
def height(self):
```
This method returns the height of the binary tree.

**7a.** Draw 7 circles and label them A, B, C, D, E, F, G.  Draw random arrows between these circles.  This will form a graph.
  * draw out the adjacency matrix and the adjacency list that corresponds to the graph

**7b.** Add some weights to your graph.  Using Dijkstra's algorithm, find the shortest path from A to every other node.

**8.** Draw a binary tree with at least 20 nodes and put in some random labels (numbers, letters, doesn't really matter as long as they are unique).

Base on this tree:
  * list the leaf nodes
  * list the root node
  * list the nodes in a preorder, postorder, inorder, breadthfirst manner
  * height of the tree
  * depth of all leaf nodes

**9a.** Create a BST tree by adding the following numbers to these trees in the order given as:

80, 70, 60, 50, 40, 30, 20, 10, 35, 45, 43

Draw the result of each tree after an insertion.


**9b.** Remove these numbers from the tree formed in 9a in the order given as: 

10, 70, 40 

Draw the result of each tree after a value is removed


**10a.** Create a min heap (smaller value, higher priority) by inserting these values in order given: 

40, 30, 10, 60, 50, 70, 20, 35, 65, 5, 7, 22, 15
Draw the result of each the tree after each insertion.

**10b.** perform remove() 3 times from your heap in 10a and draw the results.

**11.** Create an AVL tree by adding the following numbers to these trees in order given as:

80, 70, 60, 50, 40, 30, 20, 10, 35, 45, 43

Draw the result of each the tree after each insertion.

**12.** Create a Red-Black tree by adding the following numbers to these trees in order given as:

10, 20, 30, 40, 50, 60, 70, 80, 46, 56, 44, 48, 49, 78

Draw the result of each the tree after each insertion.

**13.** Create a 2-3 tree by adding the following numbers to these trees in order given as:

80, 70, 60, 50, 40, 30, 20, 65, 62, 10, 25, 21, 22

Draw the result of each the tree after each insertion.
 
**14a.** Suppose you are given the list: [15, 12, 14, 11, 10, 9, 7, 5, 2, 1].  
Draw the complete binary tree associated with the list. 

**14b.** Make heap in place using the heapify algorithm on the list in part 14a to form a **min-heap**.  Draw the final heap and state the final list created from the heapify routine.  

**15.** Given the following BST class declaration

```python
class BST:
	class Node:
		# Node's init function
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	#BST's init function
	def __init__(self):
		self.root = None
```

Write the BST class method:
```python
def inorder_successor(self, value):
```
This method returns the inorder successor of value. If there are no nodes with this value in the BST, or the node containing this value does not have an inorder succesor, this method should return None.

**16.** Is it possible to write a program that can check for infinite loops?