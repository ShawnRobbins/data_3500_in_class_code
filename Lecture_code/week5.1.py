# finding how many times X values appers in a N * N multiplication table

'''
looping
if row * col == X:
    counter += 1
'''

counter = 0
N = 10
X = 20

for row in range(1, N + 1):
    # print(row)
    for col in range (1, N + 1):
        # print(col, end="")
        # print(row, col)
    #     print(row * col, end = "\t")
        if row * col == X:
            counter += 1
    # print()
print("There are", counter, "occurances of", X)

# nested statements - refer above

# sential value - break and continue

# print("Enter numbers to average. Enter -1 to end")

# counter = 0
# total = 0

# while True:
#     counter += 1
#     num = int(input("Enter a number: "))
#     if num == -1:
#         break
#     total += num
#     avg = total/counter

# print("Average:", avg)

# range function
for i in range(5, 96, 5):
    print(i)

# break and continue
for i in range(10):
    if i == 7:
        continue
    else:
        print("i:", i)

for i in range(10):
    if i == 7:
        break
    else:
        print("i:", i)


# boolean operators
# and
# not
# or

age = 18
citizenship = False

if age == 18 and citizenship:
    print("You can vote!")
else:
    print("You can't vote")

key = True
pin = False

if key or pin:
    print("YOu can get into my parent's garage")
else:
    print("Why are you trying to break in?")


num1 = 4
num2 = 6

if num1 == 4 or num2 == 10:
    print("Those are great numbers!")
else:
    print("I don't like those numbers.")


