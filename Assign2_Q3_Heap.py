"""
PURPOSE : Find ten greatest numbers in a sequence of numbers (Q3)
AUTHOR : Manvar Nisharg (EE19B094)
DATE : 1st October 2020
INPUT : k (the number of greatest number needed) , sequence of numbers
OUTPUT : k greatest number in the sequence
NOTE : Please use python 3.x as several functions used as only compatible with python 3 or later versions
"""




#import header files
import sys

#Class to implement Min Heap Data structure
class minHeap:
	def __init__(self,max_heapsize):
		self.currentsize = 0	#Currentsize of heap
		self.maxsize = max_heapsize	 #Maxsize of heap
		self.heap = [0] * (max_heapsize + 1) 	#Initalize all nodes of heap
		self.heap[0] = -1 * sys.maxsize 	#Initalize reference node

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

	#Heapify all the nodes
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

		print("%f "%self.heap[index],end = " ")

		self.print_Heap(self.get_left_child(index))
		self.print_Heap(self.get_right_child(index))

#Call function to implement the algorithm
def ten_greatest_number():
	print()
	print("To find k greatest numbers in a sequence of n numbers")
	print()

	k = 0
	while(k <= 0): 	#Taking k as input from user untill valid input is not received
		k = int(input("Enter k (>0) : "))
		print()


	sequence = input("Enter sequence of numbers seperated by space : ") 	#Storing sequence of numbers as string (sequence)
	list_of_numbers = sequence.split() 	#Splitting sequence string into individual numbers with space as delimitter in a list (list_of_numbers)
	while len(list_of_numbers) < k: 	#If count of numbers is small than k then ask user if to still continue or input new sequence or terminate the program
		print("Input has only %d numbers i.e. < k (%d)"%(len(list_of_numbers),k))
		still_continue = int(input("Enter 1 if you want to continue with same sequence, 2 for inputing new sequence and 0 to terminate the program : "))
		print()
		if still_continue == 0: 	#If still_continue is 0 then terminate the program
			return
		if still_continue == 1: 	#If still_continue is 1 then continue with current sequence
			break
		if still_continue == 2: 	#If still_continue is 2 then input the sequence agian and repeate the process
			sequence = input("Enter sequence of numbers seperated by space : ")
		list_of_numbers = sequence.split()

	Heap = minHeap(len(list_of_numbers)+1) #Initalize min-heap

	#Add k numbers into the min-heap as base case
	for number in list_of_numbers[0:k]:
		Heap.insert_node(float(number)) 

	
	#Iterate through rest of the numbers and if it is bigger than the smallest number then add it into the heap and remove the smallest number
	for a in range(k,len(list_of_numbers)):
		if(Heap.heap[1]<float(list_of_numbers[a])):
			Heap.delete_min()
			Heap.insert_node(float(list_of_numbers[a]))
			#Heap.delete_min()


	#Printing the result
	if len(list_of_numbers) < k:
		print("The %d (as input had size less than k (%d) ) greatest numbers are :"%(list_elements_count,k))
	else:
		print("The %d greatest numbers are :"%k)
	Heap.print_Heap(1)



#Calling the function
ten_greatest_number()
