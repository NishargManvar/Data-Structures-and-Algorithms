"""
PURPOSE : Multiply two binary numbers using 'Divide and Conquer' method (Karatsuba algorithm)
AUTHOR : Manvar Nisharg (EE19B094)
#DATE : 28th September 2020
INPUT : Two binary numbers
OUTPUT : Multiplication of the numbers in binary and decimal base
#NOTE : Please use python 3.x as several functions used as only compatible with python 3 or later versions
"""

#Importing header files
import math


"""
Function to make length of two binary strings same by adding zeros at the beginning of shorter string

:string1 param: First binary string
:param type: string

:string2 param: Second binary string
:param type: string

:return type: tuple of strings in same order as parameters
"""
def make_length_equal(string1 , string2):
	#Base case
	if len(string1) == len(string2):
		pass
	
	#Add 0s at the beggining of short string
	elif len(string1) < len(string2):
		string1 = '0' * (len(string2) - len(string1)) + string1

	else:
		string2 = '0' * (len(string1) - len(string2)) + string2

	return (string1 , string2)


"""
Function to multiply two single bit numbers
i.e. multiply LSBs of the two strings provided

:string1 param: First number string
:param type: string

:string2 param: Second number string
:param type: string

:return type: int
"""
def multiply_single_digit(string1 , string2):
	return int(string1[0]) * int(string2[0])


"""
Function to add two binary strings bit by bit

:string1 param: First binary string
:string1 type: string

:string2 param: Second binary string
:string2 type: string

:return type: string
"""
def add_numbers(string1 , string2):
	result = ""
	carry = 0

	#make length of both strings same
	string1 , string2 = make_length_equal(string1 , string2)
	length = len(string1)

	#Loop through bits and add them
	for i in range(length-1 , -1 , -1):
		bit_1 = int(string1[i])
		bit_2 = int(string2[i])

		sum_bit = (bit_1 ^ bit_2 ^ carry)
		result = str(sum_bit) + result

		carry = (bit_1 and bit_2) or (bit_1 and carry) or (bit_2 and carry)

	#Add bit at MSB if carry at the end of addition is 1
	if carry == 1:
		result = '1' + result

	return result


"""
Recursive function to implement Karatsuba algorithm for two binary strings

:string1 param: First binary string
:string1 type: string

:string2 param: Second binary string
:string2 type: string

:return type: int
"""
def Karatsuba(string1 , string2):
	#Make length of strings equal
	string1 , string2 = make_length_equal(string1 , string2)

	#Base Cases
	if len(string1) == 0:
		return 0
	elif len(string1) == 1:
		return multiply_single_digit(string1 , string2)


	length = int(len(string1))
	second_half = math.ceil(length/2)

	#Divide the strings into left and right half
	string1_left = string1[:math.floor(length/2)]
	string2_left = string2[:math.floor(length/2)]

	string1_right = string1[math.floor(length/2):]
	string2_right = string2[math.floor(length/2):]

	#Calculating three results required to implement the algorithm
	result1 = int(Karatsuba(string1_left , string2_left))
	result2 = int(Karatsuba(string1_right , string2_right))
	result3 = int(Karatsuba(add_numbers(string1_left , string1_right) , add_numbers(string2_left , string2_right)))

	#Caluclate and return final product
	return result1*(1<<(2*second_half)) + (result3 - result1 - result2)*(1<<second_half) + result2


"""
Call function to implement Karatsuba algorithm

:input: Two binary numbers
:output: Multiplication of the numbers in binary and decimal base
"""
def call_for_Karatsuba():
	print()
	print("To multiply two binary numbers :")
	string1 = input("Enter binary number 1 : ")
	string2 = input("Enter binary number 2 : ")

	answer = Karatsuba(string1 , string2)

	print("\nThe product of the two numbers in decimal is %d and in binary is %s \n"%(answer , bin(answer).replace("0b","")))


#Call function
call_for_Karatsuba()


