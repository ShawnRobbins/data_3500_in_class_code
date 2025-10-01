"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""
colors = ['orange', 'blue', 'black']
print("My Favorite Colors:")
for color in colors:
    print(color)
    for letter in color:
        print(letter)
    print()

"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""


"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random

rand_list = []
for i in range(10):
    rand_list.append(random.randint(1, 100))
print("\nRandom List:", rand_list)
for i in range(len(rand_list)-1):
    if rand_list[i] % 2 == 0 and rand_list[i+1] % 2 == 0:
        print("Two even numbers are next to each other!", rand_list[i], "and", rand_list[i+1])

"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""


"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

# write a function to calculate avg for year of stock prices

file = open("/workspaces/data_3500_in_class_code/AAPL.2023.txt")
# print(file)
lines = file.readlines()
# print("lines:", lines)
print("\n", len(lines), sep="")

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

# print("prices:", prices)

def avg_calculator(prices):
    return sum(prices)/len(prices)

print("avg:", avg_calculator(prices))
print("first 5:", avg_calculator(prices[0:5]))

def avg_first_5_day(prices):
    return(sum(prices[0:5])/5)

# moving avg????

print("last 5:", avg_calculator(prices[-5:]))

"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""
# All the first steps are above. Getting list and converting it into floats.
print("First 4 days avg:", avg_calculator(prices[0:4]))
print("Last 4 days avg:", avg_calculator(prices[-4:]))


# Activity 5.2

print()

# set up iterator values and trading variables
i = 0
buy = 0
total_profit = 0

# loop through prices
for price in prices:
    if i >= 4: # only begin 4 day average once there are 4 days to backtrack to
        avg = (prices[i] + prices[i - 1] + prices[i - 2] + prices[i - 3]) / 4
        if price < avg and buy == 0: # buy conditions
            buy = price
            print("Buying at:", "\t", price)
        elif price > avg and buy != 0: # sell conditions
            trade_profit = price - buy
            print("Selling at:", "\t", price)
            print("Trade profit:", "\t", trade_profit)
            total_profit += trade_profit
            buy = 0
            
    i += 1
   
print("total_profit:", "\t", total_profit)

    
