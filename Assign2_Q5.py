"""***************************************************************************************************************
PURPOSE : To find the maximum element in a unimodal sequence of n distinct numbers (Assign-2 Q5)
AUTHOR : Manvar Nisharg (EE19B094)
DATE : 
INPUT : Unimodal sequence of n distinct numbers
OUTPUT : Maximum element in the sequence
NOTE : Please use python 3.x as several functions used are only compatible with python 3 or later versions
***************************************************************************************************************"""

"""
Modified Binary function to find the maximum number in a unimodal sequence of distinct numbers (REFER PDF FOR DETAILED EXPLANATIONS)

:param sequence: List of integers
:type sequence: List

:return: Max element of the sequence
:return type: int

:input: Null
:output: Null
"""
def binary_search_modified(sequence):
	#Initalize required variables
	list_size = len(sequence)
	start = 0 	#Index of first element of active search window
	end = list_size - 1 	#Index of last element of active wsearch wi
	#Applying loop of modified binary search
	while(start <= end):
		if start==end: 	#If start = end return number at start/end
			return sequence[start]
		
		mid = int((start+end)/2) 	#Index of middle element of active search window

		# If mid element is neither at begining or at the end of the sequence,
		# compare it with adjacent numbers and take appropriate steps
		if(mid != 0 and mid != list_size-1):
			if(sequence[mid]>sequence[mid+1] and sequence[mid]>sequence[mid-1]):
				return sequence[mid]

			elif(sequence[mid]>sequence[mid+1] and sequence[mid]<sequence[mid-1]):
				end = mid-1

			else:
				start = mid+1

		# Else if mid element is at the beginning of the sequence, compare with
		# it's right element and take appropriate steps
		elif(mid == 0):
			if(sequence[mid]>sequence[mid+1]):
				return sequence[mid]
			else:
				start = mid+1

		# Else if mid element is at the end of the sequence, compare with
		# it's left element and take appropriate steps
		else:
			if(sequence[mid]>sequence[mid-1]):
				return sequence[mid]
			else:
				end = mid - 1

"""
Initial call function to find the maximum element in a unimodal sequence of n distinct numbers

:return: Null

:input: Unimodal sequence of distinct numbers

:output: Max number in the sequence
"""
def max_in_unimodal_array():
	print()
	print("To find the maximum element in a unimodal array of n distinct numbers : ")
	
	#Asking for sequence of numbers from user till valid input is found
	sequence = input("Enter sequence of numbers seperated by space : ")
	list_of_numbers = sequence.split() 	#Splitting sequence of numbers into ini=dividual numbers and storing in a list with space as delimiter
	while len(list_of_numbers) == 0:
		print("The sequence entered contains no numbers ")
		print()
		action = int(input("Enter 1 to input the sequence again and 0 to terminate the program : "))
		if action == 1:
			sequence = input("Enter sequence of numbers seperated by space : ")
			list_of_numbers = sequence.split()
		else:
			return

	#Converting list of numbers stored as strings to int data type
	list_of_numbers = list(map(float, list_of_numbers))
	
	print()
	print("The maximum element in the unimodal array is : %f"%binary_search_modified(list_of_numbers)) #Calling modified binary search function and printing result
	print()

#Calling the initial call function
max_in_unimodal_array()