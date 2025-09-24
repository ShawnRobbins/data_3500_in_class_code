# functions
# 4 reasons programmers user functions
# 1 - Can be broken into Modules/reusability
# 2 - Debugging/testing
# 3 - Organized code
# 4 - Readability

"""
4 Things every function needs
1 - Name - Definition
2 - Arguments/parameters
3 - Main body of code
4 - Return statement
"""

def print_some_nums(num):
    print(num)
    return None

print_some_nums(8)
print()

# temperature
def f_to_c(degrees_f):
    degrees_c = (degrees_f - 32) * (5/9)
    return degrees_c

# print(f_to_c(32))
degrees_celcius = f_to_c(70)
print(degrees_celcius)

# arguments
def c_to_f():
    degrees_c = int(input("Enter the degrees in Celcius: "))
    degrees_f = 32 + (9/5) * degrees_c
    return degrees_f

print(c_to_f())

# function defaults
def order_pizza(size="medium", crust_type="normal", topping="pepperoni"):
    print("You ordered a", size, "pizza with", crust_type, "crust and", topping)
    return None

order_pizza("olives")

# add two numbers
def add_two_nums(a_num1, a_num2):
    return a_num1 + a_num2

# multiply two numbers - not allowed to use *
def multiply_two_nums(m_num1, m_num2): 
    sum = 0
    for i in range(m_num1):
        sum = add_two_nums(sum, m_num2)
    return sum
    

# exponenet two numbers - not allowed to use **
def exponent_two_nums(e_num1, e_num2):
    sum = 1
    for i in range(e_num2):
        sum = (multiply_two_nums(sum, e_num1))
    
    return sum

print(multiply_two_nums(3, 5))
print(exponent_two_nums(2, 4))
