import math
def make_length_equal(string1,string2):
	if len(string1)==len(string2):
		return (string1,string2)
	
	elif len(string1) < len(string2):
		while(len(string1)!=len(string2)):
			string1 = '0' + string1
		return (string1,string2)

	else:
		while(len(string1)!=len(string2)):
			string2 = '0' + string2
		return (string1,string2)

def multiply_single_digit(string1,string2):
	return int(string1[0])*int(string2[0])

def add_numbers(string1,string2):
	result = ""
	carry = 0

	string1,string2 = make_length_equal(string1,string2)
	length = len(string1)

	for i in range(length-1,-1,-1):
		bit_1 = int(string1[i])
		bit_2 = int(string2[i])

		sum_bit = (bit_1 ^ bit_2 ^ carry)
		#print(sum_bit,end =" ")
		result = str(sum_bit) + result
		#print(result)

		carry = (bit_1 and bit_2) or (bit_1 and carry) or (bit_2 and carry)
		#print(carry)

	if carry == 1:
		result = '1' + result

	return result

def Karastuba(string1,string2):
	string1,string2 = make_length_equal(string1,string2)

	if len(string1) == 0:
		return 0
	elif len(string1) == 1:
		return multiply_single_digit(string1,string2)

	length = int(len(string1))

	first_half = math.floor(length/2)
	second_half = math.ceil(length/2)

	string1_left = string1[:math.floor(length/2)]
	string2_left = string2[:math.floor(length/2)]

	string1_right = string1[math.floor(length/2):]
	string2_right = string2[math.floor(length/2):]

	result1 = int(Karastuba(string1_left,string2_left))
	result2 = int(Karastuba(string1_right,string2_right))
	result3 = int(Karastuba(add_numbers(string1_left,string1_right),add_numbers(string2_left,string2_right)))

	return result1*(1<<(2*second_half)) + (result3 - result1 - result2)*(1<<second_half) + result2

def call_for_Karastuba():
	print()
	print("To multiply two binary numbers :")
	string1 = input("Enter binary number 1 : ")
	string2 = input("Enter binary number 2 : ")
	answer = Karastuba(string1,string2)
	print("\nThe product of the two numbers in decimal is %d and in binary is %s \n"%(answer,bin(answer).replace("0b","")))

call_for_Karastuba()



