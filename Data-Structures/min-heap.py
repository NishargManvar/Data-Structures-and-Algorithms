#import header files
import sys

#Class to implement Min Heap Data structure
class minHeap:
	def __init__(self,max_heapsize):
		self.currentsize = 0
		self.maxsize = max_heapsize
		self.heap = [0] * (max_heapsize + 1)
		self.heap[0] = -1 * sys.maxsize

	#Function to return index of left child of a node
	get_left_child = lambda self,index : 2*index

	#Function to return index of right child of a node
	get_right_child = lambda self,index : (2*index)+1

	#Function to return index of parent of a node
	get_parent = lambda self,index : index//2

	#Function that returns if given index node is a leaf
	is_leaf = lambda self,index : index > self.currentsize//2 and index <= self.currentsize
		
	#Function to swap two nodes
	def swap_nodes(self,index1,index2):
		self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]

	#Recursive function to heapify a node
	def minHeapify(self,index):
		if self.is_leaf(index):
			return

		if self.heap[index] > self.heap[self.get_left_child(index)] or self.heap[index] > self.heap[self.get_right_child(index)]:

			if self.heap[self.get_left_child(index)] < self.heap[self.get_right_child(index)]:
				self.swap_nodes(index,self.get_left_child(index))
				self.minHeapify(self.get_left_child(index))

			else:
				self.swap_nodes(index,self.get_right_child(index))
				self.minHeapify(self.get_right_child(index))

	#Heapify the whole tree
	def minHeap_whole(self):
		for index in range (self.currentsize//2-1,0,-1):
			self.minHeapify(index)
	
	#Function to insert node in the tree at right index
	def insert_node(self,value):
		if self.currentsize >= self.maxsize:
			return 0
		self.currentsize += 1

		self.heap[self.currentsize] = value

		current_node = self.currentsize

		while self.heap[current_node] < self.heap[self.get_parent(current_node)]:
			self.swap_nodes(current_node, self.get_parent(current_node))
			current_node = self.get_parent(current_node)

	#Function to delete minimum element (i.e. head) of the tree and heapify the tree
	def delete_min(self):
		value = self.heap[1]
		self.heap[1] = self.heap[self.currentsize]
		self.currentsize -= 1
		self.minHeapify(1)
		return value

	#Printing PreOrder Traversal of the tree with node at index as root
	#For printing whole tree index = 1
	def print_Heap(self,index):
		if index > self.currentsize:
			return

		print("%d "%self.heap[index],end = " ")

		self.print_Heap(self.get_left_child(index))
		self.print_Heap(self.get_right_child(index))


print()
Tree = minHeap(15)
Tree.insert_node(5)
Tree.insert_node(10)
Tree.insert_node(-4)
Tree.insert_node(-10)
Tree.print_Heap(1)
Tree.delete_min()
print("\nPrinitng heap after deleting minimum number : ")
Tree.print_Heap(1)
print("\n\n")

