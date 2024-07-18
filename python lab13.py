1.Write a Python program to find the number of times 4 appears in the tuple. 
Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) 
Output: 3'''


tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Count the number of times 4 appears in the tuple
count_of_4 = tuplex.count(4)

print("Number of times 4 appears in the tuple:", count_of_4)

output:

Number of times 4 appears in the tuple: 3
.....................................................................................................................................................................

'''2.Write a Python program to convert a list to a tuple. 
Input: listx = [5, 10, 7, 4, 15, 3] 
Output: (5, 10, 7, 4, 15, 3)'''

listx = [5, 10, 7, 4, 15, 3]

# Convert the list to a tuple
tuplex = tuple(listx)

print("Output:", tuplex)

Output: (5, 10, 7, 4, 15, 3)
.....................................................................................................................................................................

'''3. Write a Python program to calculate the sum of the numbers in a given tuple. 
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]'''
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Calculate the sum of numbers in each tuple and store the results in a list
sums = [sum(t) for t in tuples_list]

print("Sum of numbers in each tuple:", sums)

output:
Sum of numbers in each tuple: [3, 7, 11]
.....................................................................................................................................................................
'''4.Write a python program and iterate the given tuples
 Input: 
employee1 = ("John Doe", 101, "Human Resources", 60000) 
employee2 = ("Alice Smith", 102, "Marketing", 55000) 
employee3 = ("Bob Johnson", 103, "Engineering", 75000)'''

employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Iterate over each tuple
for employee in [employee1, employee2, employee3]:
    print("Name:", employee[0])
    print("ID:", employee[1])
    print("Department:", employee[2])
    print("Salary:", employee[3])
    print()  # Empty line for better readability

output:
Name: John Doe
ID: 101
Department: Human Resources
Salary: 60000

Name: Alice Smith
ID: 102
Department: Marketing
Salary: 55000

Name: Bob Johnson
ID: 103
Department: Engineering
Salary: 75000

