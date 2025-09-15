# pseudo code

# code rock paper scissors
'''
Steps for solving/writing Rock, Paper, Scissors

Input from user(s)
or 
Random input from computer

Some kind of loop

Giant if (comparison)
    make sure there are at least two inputs
    if inputs are equal
    if inputs are greater than or less than

if we find a result
    print the result, if it's a tie or if one of the player wins
'''

# # Input from user(s)
# player1 = input("Player 1 - R, P, or S: ")
# player2 = input("Player 2 - R, P, or S: ")

# # Giant if (comparison)
# #     make sure there are at least two inputs
# if player1 == None or player2 == None:
#     print("Can't play")
# #     if inputs are equal
# if player1 == player2:
#     print("It's a tie!")
# #     if inputs are greater than or less than
# elif player1 == "R":
#     if player2 == "P":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")
# elif player1 == "P":
#     if player2 == "S":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")
# elif player1 == "S":
#     if player2 == "R":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")

# garbage collection
# import gc
# x = [1, 2, 3]
# y = x
# print("y:", y)
# del x
# gc.collect()

# debugger

peanut_allergy = True
lactose_intolerant = True

# see what foods you can have
if peanut_allergy:
    print("You can't have this PB and J")
elif lactose_intolerant:
    print("You can't have ice cream")
elif peanut_allergy and lactose_intolerant:
    print("You can't have peanut butter ice cream")