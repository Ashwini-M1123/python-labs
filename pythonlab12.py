'''1.Write a Python program and calculate the mean of the below dictionary. 

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

Output: 6.2'''

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}            # Define the dictionary

                                                # Calculate the mean of the values in the dictionary
mean_value = sum(test_dict.values()) / len(test_dict)
print(mean_value)                               # Print the mean value

output:
6.2
.....................................................................................................................................................................


'''2.Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary : 

dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''


dic1 = {1: 10, 2: 20} #define the dictionaries
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result_dict = {}                        #create a new dictionary and concatenate the dictionaries

result_dict.update(dic1)                #update result_dict1 with dic1
result_dict.update(dic2)                #update result_dict with dic2
result_dict.update(dic3)                #update result_dict with dic3

                                        # Print the concatenated dictionary
print("Concatenated Dictionary:", result_dict)
output:
Values:
10
20
30
40
50
60
.....................................................................................................................................................................

'''3.Write a Python program to get the key, value and item in a dictionary. 

input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Accessing keys and values
print("Keys:")
for key in dict_num:
    print(key)

print("\nValues:")
for key in dict_num:
    print(dict_num[key])

# Accessing key-value pairs (items)
print("\nKey-Value Pairs:")
for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}")

output:
Key-Value Pairs:
Key: 1, Value: 10
Key: 2, Value: 20
Key: 3, Value: 30
Key: 4, Value: 40
Key: 5, Value: 50
Key: 6, Value: 60
