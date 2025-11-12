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


"""
Programming Activity 3

Write a program, which loads a json file "person.json" into a Python 
dictionary. Change the contents of person["age"] by adding 1. Save the 
updated dictionary to person.json, and verify the contents of person.json 
have been updated.
- load person.json in to a Python dictionary using the json.load() function
- update the value of person["age"], increase by 1
- save the Python dictionary to person.json
- open person.json and verify the "age" value has increased by 1
"""
import json

person = json.load(open("/workspaces/data_3500_in_class_code/person-2.json"))
person["age"] = person["age"] + 1

json.dump(person, open("/workspaces/data_3500_in_class_code/Programming_Activities/person.json", "w"), indent=4)

"""
Programming Activity 4

Write a program that asks the user for two numbers. In a try statement, 
attempt to divide number 1 by number 2.  If number 2 is a 0, print a 
message in the except statement saying "Error, attempted to divide by zero"
- create two variables, inputted by the user
- in a  try: block attempt to divide num1 by num2
- in a except: block print a message indicating divide by zero error
- end program
"""
num1 = input("Enter first num: ")
num2 = input("Enter second num: ")

try:
    result = int(num1)/int(num2)
    print("result:", result)
except:
    print("Error, attempted to divide by zero")