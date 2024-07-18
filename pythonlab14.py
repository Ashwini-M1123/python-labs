1.Write a Python program to Get Only unique items from two sets. 
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
Output: {70, 40, 10, 50, 20, 60, 30}'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.union(set2)

print(unique_items)

output:
{70, 40, 10, 50, 20, 60, 30}
.....................................................................................................................................................................

'''2. Write a Python program to Return a set of elements present in Set A or B, but not both.
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
Output: {20, 70, 10, 60}'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1 ^ set2
print("Output:", result)

output:
Output: {20, 70, 10, 60}
....................................................................................................................................................................

'''3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements. 
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {60, 70, 80, 90, 10} 
Output: {10}'''

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

common_elements = set1 & set2

if common_elements:
    print("Output:", common_elements)
else:
    print("No common elements found.")

output:
Output: {10}
....................................................................................................................................................................

'''4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
Output: {40, 50, 30}'''

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
common_elements = set1 & set2
print(common_elements)
 output:
{40, 50, 30}
