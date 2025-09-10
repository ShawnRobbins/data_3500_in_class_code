#Dynamic Typing

# print("I love Wednesdays because they are so fun!")
# how_much_i_love_wednesdays = 27
# print("This is how much I love Wednesday:", how_much_i_love_wednesdays)

# age = input("How old are you? ")
# print("You are " + eval(age) + " years old.")

# age = eval(input("How old will you be next year: "))
# age = age - 1
# print("That means you are", age, "years old this year!")

# float()
# string()
# int()
# bool()
# eval()

# if statements
# if something >, <, >=, <=, ==:
# do some kind of logic

# erin_vote = int(input("enter the votes for Erin: "))
# isaac_vote = int(input("enter the votes for Isaac: "))

# if erin_vote > isaac_vote:
#     print("Erin wins!")
# elif(erin_vote < isaac_vote):
#     print("Isaac wins!")
# elif(erin_vote == isaac_vote):
#     print("It's a tie!!! Co-presidents!")
# else:
#     print("Something went wrong.")


# input, the default type will be a string

# min max range
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))

# print(min(num1, num2. num3))

# Aggie Basketball
'''
If you are a student, you get in for free
If you have HURD premium, you get in 15 min early
If you aren't either of these, you need to buy a ticket
If you're faculty, you still need to buy a ticket, but you get a discount
'''

student = input("Are you a USU student? (yes/no): ")
HURD = input("Are you a member of HERD premium? (yes/no): ")


if student == "yes":
    print("You get in for free!")
    if HURD == "yes":
        print("and you can get in 15 minutes early!")
elif student ==  "no":
    faculty = input("Are you a USU faculty member? (yes/no): ")n
    print("You have to buy a ticket.")
    if faculty == "yes":
        print("But you can get a discount!")
    elif faculty == "no":
        print("At full price.")
