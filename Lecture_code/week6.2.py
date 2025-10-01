# list slicing

states = ["North Carolina", "Wyoming", "Texas", "Massachusetts", "Pennsylvania", "Arizona", "Utah", "alabama"]

# index of MA
print(states[3])

# slice operator
subset1 = states[1:4]
print("subset1:", subset1)

# just the last element of our list
last_element = states[-1:]
print("last element:", last_element)

# reverse a list
reversed_states = states[::-1]
print("reversed states:", reversed_states)

# return everything except for the last two elements
subset2 = states[:-2]
print("subset2:", subset2)

# every other element
subset3 = states[::2]
print("subset3:", subset3)

# reversed
states.reverse()
print("reversed 2:", states)

# sort 
states.sort()
print("sorted states:", states)