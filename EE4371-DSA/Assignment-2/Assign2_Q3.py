#***********************************************************************************************************************************************
#PURPOSE : EE4371 Assignment 2 - Q3 (Find k greatest numbers in sequence of n numbers)
#AUTHOR : Manvar Nisharg (EE19B094)
#DATE : 
#INPUT : k, sequence of numbers, if repetations are to be discarded
#OUTPUT : k greatest numbers in the sequence (They are also sorted as a side effect of the algorithm implemented although not asked in the question)
#NOTE : Please use python 3.x as several functions used as only compatible with python 3 or later versions
#		Please refer to PDF for explanation of the algorithm used in the code
#***********************************************************************************************************************************************

#Class defining the node for linked list
#Node has two parameters: 1) value of node 2) pointer to next node
class node:
	def __init__(self,val=None): 	#Initalize node with node value as 'val' and pointer as Null
		self.value = val 	#Value of node
		self.nextnode = None 	#Pointer to next node




#Class containing linkedlist functions/methods
class LinkedList:
	def __init__(self): 	# Function to initalize linkedlist
		self.head = None 	# Initalize linkedlist by initalizing pointer to head as NULL


#PURPOSE : Function to add node into the sorted linkedlist such that the list remains sorted
#PARAMETERS : Pointer of head i.e the object , The number to be added (number) , to add the number or not if number is already present in the list (repeate)(1 for NO and 0 for YES)
#RETURN VALUE : 1 if number is added in the list, 0 otherwise
#CONSOLE INPUT : Null
#CONSOLE OUTPUT : Null
	def addnode(self,number,repeate):
		if self.head is None: 	#If no element is present in the list i.e. head pointer is Null
			self.head = node(number) 	#Initalize node at head pointer with node value as number
			return 1 	#Return 1 as a node is added into the list

		#Compare the number with head
		if(repeate and self.head.value == number): 	#If repeate is 1 and number is same as head value then don't add the number and return 0
			return 0
		if self.head.value >= number: 	#Else if number is <= the head value then add the node before head
			temp_node = node(number) 	#Initalize the new node with node value as number
			temp_node.nextnode = self.head 	#Pointing the pointer of new node to head 
			self.head = temp_node 	#Changing head pointer to new node
			return 1 	#return 1 as node is added into list

		#Traverse through the list and compare the value of node and number
		temp = self.head 	#Loop variable for looping through the list
		while temp.nextnode is not None: 	#Looping till we reach end of loop
			if (repeate and temp.nextnode.value == number): 	#If repeate is 1 and number is same as node value then don't add the number and return 0
				return 0
			if temp.nextnode.value >= number : 	#If number is <= the node value then add number into list
				temp_node = node(number) 	#Initalzing new node to add into the list with node value as number
				temp_node.nextnode = temp.nextnode 	#Pointing the pointer of new node to the next node
				temp.nextnode = temp_node 	#Pointing the pointer of previous node to new node
				return 1 	#Return 1 as node is added
			temp = temp.nextnode 	#Else move the loop node to the next node

		#If no node value in list is > than number then add new node at end of list
		temp_node=node(number) 	#Initalize new node to add into the list with node value as number
		temp.nextnode = temp_node 	#Pointing the pointer of previous node to new node
		return 1 	# Return 1 as node is added into the list


#PURPOSE : Add a number into the list if it is greater than the smallest number (i.e head of list) in the list and then removing the smallest number
#PARAMETERS : Pointer of head i.e. the object , the number to be added (number) , to add the number or not if number is already present in the list (repeate)(1 for NO and 0 for YES)
#RETURN VALUE : 1 if number is added in the list, 0 otherwise
#CONSOLE INPUT : Null
#CONSLOE OUTPUT : Null
	def check_and_addnode(self,number,repeate):
		if repeate and self.head.value == number: 	#If repeate is 1 and value of head is same as number don't add number into list and retuen 0
			return 0
		if self.head.value < number: 	#If value of head is < number, therefore number needs to be added in the list
			if self.addnode(number,repeate): 	#Call the addnode method to add the node in the list at appropriate place in the list so that list reamisn sorted
				temp = self.head 	#Storing head pointer to temporary variable to free memory later
				self.head = self.head.nextnode 	#Changing head pointer to the node after head thus removing the old head node from the list
				temp = None 	#Freeing memory
				return 1	 #Return 1 as node is added
			return 0 	#Else return 0 as node is not added			


#PURPOSE : Function to be call to implement the algorithm (Find k greatest numbers in sequence of n numbers)
#PARAMETERS : Null
#RETURN VALUE : Null
#CONSOLE INPUT : k, sequence of numbers, if repetations are to be discarded
#CONSOLE OUTPUT : k greatest numbers in the sequence (provided that many numbers are present in the sequence else appropriate output is printed)
#NOTE : This function makes calls to other functions/methods i.e. addnode() and check_and_addnode() methods in Linkedlist class
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


	repeate = int(input("Enter 0 if duplicates are to be counted and 1 if they are to be discarded : ")) 	#Ask user if duplicates need to be discarded or not
	print()


	ll = LinkedList() #Initalize linkedlist
	
	#Add k numbers into the linkedlist in sorted number as base case
	count = 0	#Count variable to keep count of numbers added in the linkedlist
	x = 0 	#Loop index for traversing through the list
	while count != k and x < len(list_of_numbers): 	#Add numbers into linkedlist till count becomes k or we reach end of list
		if ll.addnode(int(list_of_numbers[x]),repeate): 	#Try adding number into linkedlist using addnode and if number is added increase count by 1
			count = count + 1
		x = x + 1 	#Increase loop index by 1

	for a in range(x,len(list_of_numbers)): 	#For remaining numbers in the list add them in place of the smallest number in the linkedlist if they are bigger then them
		ll.check_and_addnode(int(list_of_numbers[a]),repeate)

	list_elements_count = 0 	#Variable to count the number of final elements in the linkedlist
	temp = ll.head 	#Looping through the lisnkedlist and count number of nodes
	while temp is not None :
		list_elements_count = list_elements_count + 1
		temp = temp.nextnode

	#Prining appropriate result statement for various cases
	if len(list_of_numbers) < k:
		print("The %d (as input had size less than k (%d) ) greatest numbers are :"%(list_elements_count,k))	
	elif list_elements_count < k and repeate == 1:
		print("There were only %d unique numbers in the sequence after discarding duplicates"%list_elements_count)
		print("Therefore the %d greatest numbers are :"%list_elements_count)
	elif repeate == 1:
		print("The %d greatest numbers after removing duplicates are"%k)
	else:
		print("The %d greatest numbers are"%k)
	
	#Printing the conntent of the linkedlist		
	temp = ll.head
	while temp is not None :
		print(temp.value,end = " ")
		temp = temp.nextnode
	print()
	return


ten_greatest_number() 	#Calling the function