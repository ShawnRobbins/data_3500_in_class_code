"""
Programming Activity 1

Create a list with your 3 favorite colors. Display the message:
"My favorite colors are: blue, white, red" , 
but use the string join function to turn the list into a comma separated string.
- create a list with 3 favorite colors: ["blue", "white", "red"]
- create a string with value "My favorite colors are: "
- convert list to a comma separated string using join()
- concatenate the two strings and print the message
"""
favColors = ["orange", "blue", "black"]
colorStr = "My favorite colors are: "
favColors = ", ".join(favColors)
colorStr = colorStr + favColors
print(colorStr)

"""
Programming Activity 2

Write a program which asks the user to enter their address
Use the isalnum() function to verify the entered a valid address
- create a variable that stores the string address the user enters
- remove white space from the string
- use isalnum() on the string with no whitespace to verify all characters 
are numbers or letters
"""

userAddress = input("Enter your address: ")
addressList = userAddress.strip().split(" ")
cleanAddress = "".join(addressList)
print(cleanAddress.isalnum())