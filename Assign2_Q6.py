"""***********************************************************************************************************
PURPOSE : Remove duplicates from a sequence of numbers (Assign-2 Q6)
AUTHOR : Manvar Nisharg (EE19B094)
DATE :  29th Sept 2020
INPUT : Sequence of numbers
OUTPUT : Sequence of numbers with duplicates removed in sorted and original form
NOTE : Please use python 3.x as several functions used as only compatible with python 3 or later versions
**********************************************************************************************************"""

from array import array #Importing necessary files

"""
Function to merge two sorted subarrays into one

:param arr: The array whose two subarrays are to be merged
:param type: list
:param start: The starting index in arr from where elements are to be merged(i.e. starting index of first subarray)
:param type: int
:param mid: The midpoint index in arr (i.e. index where two subarrays are to be divided)
:param type: int
:param end: The endpoint index in arr till where elements are to be merged(i.e. ending index of second subarray)
:param type: int
"""
def merge(arr, start, mid, end): 
    #size of arrays to be merged
    size_left = mid - start + 1
    size_right = end - mid 
  
  
    ##Initalize temporary arrays and copy data from original arrays to temporary arrays
    temp_left = arr[start : start + size_left]
    temp_right = arr[start + size_left : end+1]
 
   
    #Pointers to current elements in all three arays
    i = 0     # Initial index of first temporary array
    j = 0     # Initial index of second temporaary array 
    k = start     # Initial index of merged array 
  
    #Comparing elements and adding them into the original array until end of any one array is reached
    while i < size_left and j < size_right : 
        if temp_left[i] <= temp_right[j]: 
            arr[k] = temp_left[i] 
            i += 1
        else: 
            arr[k] = temp_right[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of temp_left array if any, into the original array
    while i < size_left: 
        arr[k] = temp_left[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of temp_right array if any, into the original array  
    while j < size_right: 
        arr[k] = temp_right[j] 
        j += 1
        k += 1


"""
Function to sort a array using merger sort algorithm

:param arr: The array which is to be merged
:param type: list
:param start: The index of first element to be sorted
:param type: int
:param end: The index of last element to be sorted
:param type: int
"""
def mergeSort(arr,start,end): 
    if start >= end:
        return 
  
    mid = (start+(end-1))//2
  
    # Dividing array into two halves and sorting both the halves first
    mergeSort(arr, start, mid) 
    mergeSort(arr, mid+1, end) 
    # Merging the already sorted arrays into one
    merge(arr, start, mid, end)



"""
Function to return index of a number in a sorted 2D array using binary search algorithm (w.r.t. first coloumn)

:param arr: The arr in which number is to be searched
:param type: list
:param number: The number to be searched
:param type: float

:return: index of number in array
"""
def binary_search(arr,number):
    #Base Cases
    if(len(arr)==0):
        return
    elif(len(arr)==1):
        return 0

    #Initalize pointers to beginning and end of array
    start = 0
    end = int(len(arr)-1)

    while start <= end:
        
        mid = int((start + end)/2)  #Middle index of active window of search

        if(arr[mid][0] == number):     #If number at mid is equal to 'number' then return mid
            return mid
        elif(arr[mid][0] > number):  #Else if number at mid is greater than 'number' then change end pointer to mid-1
            end = mid - 1
        else:    #Else if number at mid is less than 'number' then change start pointer to mid+1
            start = mid + 1

    return -1   #If number is not found return -1


"""
Call function to remove duplicates from a sequence of numbers

:input: Sequence of numbers
:output: Sequence of numbers with duplicates removed in sorted and original form
"""
def remove_duplicates():
    print("\nTo remove duplicates from a sequence of numbers :")
    
    sequence = input("Enter sequence of numbers seperated by space : ")     #Storing sequence of numbers as string (sequence)
    list_of_numbers_original = sequence.split()  #Splitting sequence string into individual numbers with space as delimitter in a list (list_of_numbers_original)
    while len(list_of_numbers_original) == 0:     #If count of numbers is 0 then ask user if to input new sequence or terminate the program
        print("Input has only no numbers ")
        still_continue = int(input("Enter 1 for inputing new sequence and 0 to terminate the program : "))
        print()
        if still_continue == 0:     #If still_continue is 0 then terminate the program
            return
        if still_continue == 1:     #If still_continue is 1 then input the sequence agian and repeate the process
            sequence = input("Enter sequence of numbers seperated by space : ")
        list_of_numbers_original = sequence.split()
    print()

    list_of_numbers_original = list(map(float, list_of_numbers_original))   #Converting numbers stored as string to int
    list_of_numbers = list_of_numbers_original.copy()   # Making a copy of original list for processing

    mergeSort(list_of_numbers,0,len(list_of_numbers)-1)     # Sorting the list of numbers using merge-sort


    #Initalize an empty 2D array whose first coloumn will contain all the sorted numbers once and
    #second coloumn contains if that number has already been printed or not (0 for NO and 1 for YES)
    #so initially 0 for all
    #This array will be used later to print sequence in original order
    binary_array_for_numbers = []
    


    #Prining sorted list so that one number is printed only once
    
    print("The sequence with duplicates removed in sorted order :")
    current = list_of_numbers[0]    #Initalize variable which stores value of active number
    print(list_of_numbers[0],end=" ")   #Printing first element
    
    #Adding number into binary_array_for_numbers array as it is encountered for first time
    temp = []
    temp.append(list_of_numbers[0])
    temp.append(0)
    binary_array_for_numbers.append(temp)
    
    #Looping through list from index 1 to end
    for i in range(1,len(list_of_numbers)):
        if list_of_numbers[i] == current:   #If number at index i is same as current then it has already been printed so continue
            continue
        else:
            print(list_of_numbers[i],end = " ")     #Else the number has occured first time so print it and change the value of current to that value
            current = list_of_numbers[i]
            #Adding number into binary_array_for_numbers array as it is encountered for first time
            temp = []
            temp.append(list_of_numbers[i])
            temp.append(0)
            binary_array_for_numbers.append(temp)
    print()
    print()



    #Printing sequence with duplicates removed in original order
    
    print("The sequence with duplicates removed in original order is :")

    #Looping through the numbers in the original list given by user
    for i in range(len(list_of_numbers_original)):
        index = binary_search(binary_array_for_numbers,list_of_numbers_original[i])  #Finding index of that number in binary_array_of_numbers using binary search
        if(binary_array_for_numbers[index][1] == 1):    #If the value of second coloumn is 1 for that index that means number has alrady been printed
            continue
        else:
            print(binary_array_for_numbers[index][0],end = " ")     #Else print the number and change value of second coloumn to 1
            binary_array_for_numbers[index][1] = 1


remove_duplicates() #Calling function to remove duplicates



