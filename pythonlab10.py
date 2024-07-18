#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers(a,b):
    try:
        result=a/b
        print("the result of {a} divided by {b} is: {result} ")
    except ZeroDivisionError:
        print("Error:cannot divide by zero!")
a=10
b=0
divide_numbers(a,b)

output:
Error:cannot divide by zero!
.....................................................................................................................................................................

#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_valid_integer(prompt):
    while True:
        try:
            value = input(prompt)                   # Try converting the input to an integer
            integer_value = int(value)
            return integer_value                    # If successful, return the integer value
        except ValueError:
                                                    # If conversion to integer fails, handle the exception
            print("Error: Please enter a valid integer.")
user_integer = get_valid_integer("Please enter an integer: ")# Prompt the user to input an integer
print("You entered:", user_integer)

output:
Please enter an integer: a
Error: Please enter a valid integer.
Please enter an integer: 4
You entered: 4
.....................................................................................................................................................................

#3.write a python program that opens a file and handles a fileNotFoundError exception if the file does not exist.

def read_file_contents(filename):
    try:
        # Attempt to open the file for reading
        with open(filename, 'r') as file:    # Attempt to open the file for reading
            contents = file.read()
            print("File contents:")          # Read and print the file contents
            print(contents)
    except FileNotFoundError:                # Handle the case where the file is not found
        print(f"Error: The file '{filename}' does not exist.")
file_name = input("Enter the filename: ")    # Prompt the user to enter the filename
read_file_contents(file_name)                # Call the function to read and handle the file

output:
Enter the filename: abc.txt
Error: The file 'abc.txt' does not exist.
.....................................................................................................................................................................
#4. write a python program that prompts the user to input two numbers and raises a Type error exception if the inputs are not numerical.

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid numerical value.")

try:
    num1 = get_valid_number("Enter the first number: ")     # Prompt the user to input the first number
    num2 = get_valid_number("Enter the second number: ")    # Prompt the user to input the second number
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")     # Print the sum of the two numbers

except TypeError:
    print("Error: Non-numeric input detected.")

output:
Enter the first number: 2
Enter the second number: 3
The sum of 2.0 and 3.0 is: 5.0
