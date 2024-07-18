**________________________________Assignment -1 __________________________**

Lab1: Write a python program to read the radius from the below .csv file
and then Calculate the Area of a Circle using SciPy Constants. After that display
the first 5 records and also save the calculated result into a new .csv file.

Input:
https://raw.githubusercontent.com/AnudipAE/DANLC/master/radius_data.csv

CODE:

import pandas as pd
from scipy.constants import pi

# Step 1: Read the radius data from the CSV file
url = "https://raw.githubusercontent.com/AnudipAE/DANLC/master/radius_data.csv"
df = pd.read_csv(url)

# Step 2: Calculate the area of a circle for each radius
df['Area'] = pi * (df['Radius'] ** 2)

# Step 3: Display the first 5 records and their areas
print("First 5 records with calculated areas:")
print(df.head())

# Step 4: Save the results to a new CSV file
output_csv = "radius_area_results.csv"
df.to_csv(output_csv, index=False)

print(f"\nResults saved to {output_csv}")


OUTPUT:

First 5 records with calculated areas:
  CircleName    Radius        Area
0        SAY  3.798717   45.333960
1        PSN  9.958397  311.550720
2        JDP  5.142711   83.087197
3        AUO  3.319584   34.619210
4        OHG  1.138395    4.071325




**________________________________Assignment -2 __________________________**

Lab4: Write a python program to read the GB from the below .csv file and
then Convert GB to MB using SciPy Constants. After that display the first 5
records and also save the calculated result into a new csv file.

Input:
https://raw.githubusercontent.com/AnudipAE/DANLC/master/file_size.csv

CODE:

import pandas as pd
from scipy.constants import giga, mega

# Step 1: Read the CSV file from the URL
url = "https://raw.githubusercontent.com/AnudipAE/DANLC/master/file_size.csv"
df = pd.read_csv(url)

# Step 2: Convert GB to MB
df['Size_in_MB'] = df['Size in GB'] * giga / mega

# Step 3: Display the first 5 records
print("First 5 records after conversion:")
print(df.head())

# Step 4: Save the result to a new CSV file
output_filename = "file_size_MB.csv"
df.to_csv(output_filename, index=False)
print(f"\nConverted data saved to '{output_filename}'")

OUTPUT:


First 5 Records:
  Filename    Size (GB) Size (MB)
0 file_1.txt  9720.0    9.72
1 file 2.txt  9810.0    9.81
2 file_3.txt  5610.0	5.61
3 file_4.txt  4580.0	4.58
4 file_5.txt  5520.0	5.52



**________________________________Assignment -3 __________________________**

CHATGPT:

Scenario:Calculate the Escape Velocity of a Rocket from Earth Suppose you're working on a space exploration project, and you need to calculate the
escape velocity of a rocket to leave Earth's gravitational field. You can use SciPy constants to make calculations like Calculate the escape velocity, Mass
of Earth (kg),Radius of Earth (m). Create a ChatGPT prompt to generate the code for this scenario. Based on the code generated, ask ChatGPT to give the
conclusion/inference.



CODE:
from scipy.constants import G

# Constants
mass_of_earth = 5.972e24  # kg (mass of Earth)
radius_of_earth = 6371e3  # m (radius of Earth)

# Calculate escape velocity
escape_velocity = (2 * G * mass_of_earth / radius_of_earth)**0.5

print(f"The escape velocity from Earth's surface is approximately {escape_velocity:.2f} m/s")


OUTPUT:
The escape velocity from Earth's surface is approximately 11185.98 m/s

