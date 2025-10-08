import numpy as np
"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""
name = input("What is your name? ")  
fav_color = input("What is your favorite color? ")
with open("ColorFile.txt", "w") as cFile:
    cFile.write(name + "'s favorite color is " + fav_color + ".")

"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""

arr = np.zeros(100)
print(arr)
arr = np.random.rand(100)
print(arr)
 

#Additional Challenge Question

"""
Write a program, which loads a json file "person.json" into a Python 
dictionary. Change the contents of person["age"] by adding 1. Save the 
updated dictionary to person.json, and verify the contents of person.json 
have been updated.
- load person.json in to a Python dictionary using the json.load() function
- update the value of person["age"], increase by 1
- save the Python dictionary to person.json
- open person.json and verify the "age" value has increased by 1
"""