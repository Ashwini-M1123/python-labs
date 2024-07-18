#1.write a python program to sum all the items in a list

def sum_list_items(lst):
    total_sum=sum(lst)
    return total_sum
my_lst=[10,20,30,40,50]
result = sum_list_items(my_lst)                         #calculate the sum of all items in the list
print(f"the sum of all items in the list is:{result}")  #display the result

output:
the sum of all items in the list is:150
.....................................................................................................................................................................

#2.Write a Python program to get the largest and smallest number from a list without builtin functions.def find_largest_smallest(lst):
def find_largest_smallest(lst):
    if not lst:
        return None, None                   #Return None for both largest and smallest if the list is empty
    
    largest = lst[0]
    smallest = lst[0]
    
    for num in lst:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
            
    return largest, smallest
my_list = [10, 5, 20, 8, 15]

                                        # Call the function to find the largest and smallest numbers
largest_num, smallest_num = find_largest_smallest(my_list)
                                        # Display the results
if largest_num is not None and smallest_num is not None:
    print(f"The largest number in the list is: {largest_num}")
    print(f"The smallest number in the list is: {smallest_num}")
else:
    print("The list is empty.")

output:
The largest number in the list is: 20
The smallest number in the list is: 5
.....................................................................................................................................................................


#3.Write a Python program to find duplicate values from a list and display those.
def find_duplicates(lst):
    counts = {}                                 # Dictionary to store element counts
    duplicates = []

    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

                            # Append elements with count > 1 to duplicates list
    for key, value in counts.items():
        if value > 1:
            duplicates.append(key)

    return duplicates
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 1]
result = find_duplicates(my_list)
if result:
    print("Duplicate elements:", result)
else:
    print("No duplicates found.")    

output:

Duplicate elements: [1, 2, 3]
.....................................................................................................................................................................

'''4.Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

Original list: [1, 1, 2, 3, 4, 4, 5, 1] 

Length of the first part of the list: 3 

Splitted the said list into two parts: 

([1, 1, 2], [3, 4, 4, 5, 1])'''

def split_list(lst, first_part_length):
    first_part = lst[:first_part_length]
    second_part = lst[first_part_length:]
    return (first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3

result = split_list(original_list, length_of_first_part)
print("Splitted the said list into two parts:")
print(result)

output:
Splitted the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])
.....................................................................................................................................................................

'''5.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order:

black 

white 

green 

red'''


original_list = ['red', 'green', 'white', 'black'] # Original list
for index, value in reversed(list(enumerate(original_list))): # Traverse the list in reverse order
    print(f"{value} (index {index})")
output:
black (index 3)
white (index 2)
green (index 1)
red (index 0)


