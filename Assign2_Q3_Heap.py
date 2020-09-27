class minHeap:
	def __init__(self,max_heapsize):
		self.currentsize = 0
		self.maxsize = max_heapsize
		self.heap = [0] * (max_heapsize + 1)
		self.heap[0] = -1 * max_heapsize

	def get_left_child(self,index):
		return 2*index

	def get_right_child(self,index):
		return (2*index)+1

	def get_parent(self,index):
		return index//2

	def isLeaf(self,index):
		if index >= self.currentsize//2 and index <= self.currentsize:
			return 1
		return 0

	def swap_nodes(self,index1,index2):
		self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]

	def minHeapify(self,index):
		if not self.isLeaf(index):
			if self.heap[index] >= self.heap[self.get_left_child(index)] or self.heap[index] >= self.heap[self.get_right_child(index)]:

				if self.heap[self.get_left_child(index)] <= self.heap[self.get_right_child(index)]:
					self.swap_nodes(index,self.get_left_child(index))
					self.minHeapify(self.get_left_child(index))

				else:
					self.swap_nodes(index,self.get_right_child(index))
					self.minHeapify(self.get_right_child(index))

	def minHeap_whole(self):
		for index in range (self.currentsize//2-1,0,-1):
			self.minHeapify(index)
	
	def insert_node(self,value):
		if self.currentsize >= self.maxsize:
			return 0
		self.currentsize += 1

		self.heap[self.currentsize] = value

		current_node = self.currentsize

		while self.heap[current_node] < self.heap[self.get_parent(current_node)]:
			self.swap_nodes(current_node, self.get_parent(current_node))
			current_node = self.get_parent(current_node)

	def print_Heap(self,index):
		if index > self.currentsize:
			return

		print("%d "%self.heap[index],end = " ")

		self.print_Heap(self.get_left_child(index))
		self.print_Heap(self.get_right_child(index))

	def delete_min(self):
		value = self.heap[1]
		self.heap[1] = self.heap[self.currentsize]
		self.currentsize -= 1
		self.minHeapify(1)
		return value

def ten_greatest_number():
	print()
	print("To find k greatest numbers in a sequence of n numbers")
	print()

	k = 0
	while(k <= 0): 	#Taking k as input from user untill valid input is not received
		k = int(input("Enter k (>0) : ")) 	#Storing the value in k
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

	Heap = minHeap(len(list_of_numbers))

#Add k numbers into the linkedlist in sorted number as base case
	count = 0	#Count variable to keep count of numbers added in the linkedlist
	x = 0 	#Loop index for traversing through the list
	while count != k and x < len(list_of_numbers): 	#Add numbers into linkedlist till count becomes k or we reach end of list
		Heap.insert_node(int(list_of_numbers[x])) 	#Try adding number into linkedlist using addnode and if number is added increase count by 1
		count = count + 1
		x = x + 1 	#Increase loop index by 1

	Heap.print_Heap(1)
	print()


	for a in range(x,len(list_of_numbers)):
		if(Heap.heap[1]<int(list_of_numbers[a])):
			Heap.insert_node(int(list_of_numbers[a]))
			Heap.print_Heap(1)
			print("%d"%Heap.delete_min())

	if len(list_of_numbers) < k:
		print("The %d (as input had size less than k (%d) ) greatest numbers are :"%(list_elements_count,k))
	else:
		print("The %d greatest numbers are :"%k)
	Heap.print_Heap(1)


ten_greatest_number()
