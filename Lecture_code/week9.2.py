# Strings

# concatenation
print("hello " + "world")

#var = input("Enter something: ")

print("hello", "world" + " I love " + "python")

fruit = "apple"
print("fruit:", fruit)
fruit *= 20
print("fruit:", fruit)

# string whitespace
example = "\tProfessor H      \t\t\t\n hello :)\t"
print("Example: ", example)
print(example.strip())
print(example.rstrip())
print(example.lstrip())

# capitalization stuff
name = "big blue"
print("capitalize:", name.capitalize())
print("upper:", name.upper())
print("is upper?:", name.isupper())
print("is lower?:", name.islower())
print("lower:", name.lower())
print("is digit?:", name.isdigit())

# get user input
cities = []
for i in range(5):
    city = input("Enter the city you are from: ").lower()
    if city in cities:
        pass
    else:   
        cities.append(city)

