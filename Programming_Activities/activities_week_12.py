"""
Programming Activity 1

Write a program which asks the user for two numbers, stored in two variables num1 and num2. 
Generate a multiplication table for all integers 1 through num1 and 1 through num2. 
The bottom right entry in your table should have the product of num1 and num2. 
The table must be stored in a 2D list. 
The list must be created first with a nested for loop. 
Then, the table should be printed by another nested for loop iterating through the 2D list.
Steps:
- store the variables.
- create a list, and add empty lists to the list - however many your need from the variables above.
- append the values to the lists.
- use a nested for loop to iterate through the list and print the values.
"""
print("Mult Table Maker!")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
table = []
for i in range(num2):
    table.append([])

for i in range(1, num1+1):
    for j in range(1, num2+1):
        table[j-1].append(i*j)
#print(table)
for list in table:
    for entry in list:
        print(entry, end="\t")
    print()
"""
Programming Activity 2

Write a program which asks the user their age and favorite color.  
Store these values in a dictionary with keys "age" and "favorite_color".  
Also save the 2D list from the previous activity in the dictionary with the 
key "multiplication_table".
print all the values in the dictionary by iterating through the keys 
using a for loop.
"""

age = int(input("How old are you? "))
fav_color = input("What is your favorite color? " )

act_2_dict = {"age":age, "fav_color":fav_color, "multiplication_table":table}
for key in act_2_dict.keys():
    print("Key:", key, "Value:", act_2_dict[key])