"""
Programming Activity 1

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""
evenLst = [i for i in range(2, 101, 2)]
print(evenLst)
"""
Programming Activity 2

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""
def trimStrings(stringList):
    trimmedStrings = [string.strip() for string in strings]
    return trimmedStrings

strings = ["    front", "back     ", "     both      ", "none"]
print(trimStrings(strings))

"""
Programming Activity 3

Write a Python program which asks the user their name.  
Store their name in a string variable. Use the Upper() function to make 
all of the letters in their name upper case. Then, print to the console: 
welcome, NAME ALLCAPS!.
 - using input get the user name
 - change the string to be all upper case
 - print to the console: "welcome, NAME ALLCAPS!" (adding an exclamation
"""
print()
name = input("Please enter your name: ")
def upperName(name):
    upper = name.upper()
    print("Welcome, ", upper, "!", sep="")
upperName(name)

"""
Programming Activity 4

Create a variable that stores the sentence below, and print the sentence to 
the console, before making any changes. Change the first letter in the 
sentence to be capitalized. Change the first instance of Whoa to be whoa 
(all lower case), and the second instance of Whoa to be WHOA(all upper case).  
Append a exclamation point to the end of the sentence. 
Then re-print the sentence to the console.

sentence = "dude, I just biked down that mountain and at first I was like 
Whoa, and then I was like Whoa"
 - using the string variable sentence, change the first letter to upper 
   case using capitalize()
 - create a list called "words" that stores all the words in the sentence 
   in a list using the split() function.
 - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
 - append an exclamation point.
 - print the new sentence.
"""

sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"
def woahify(sentence):
    sentence = sentence.capitalize()
    words = sentence.split(" ")
    first_whoa = True
    i = 0
   # print(words)
    for word in words:
        if words[i][:4] == "whoa" and first_whoa:
            print("changing first whoa")
            first_whoa = False
        elif words[i] == "whoa" and not first_whoa:
            words[i] = words[i].upper()
        else:
            pass
        i += 1
    words.append("!")
    for word in words:
        print(word, end=" ")
woahify(sentence)

 

# Additional Challenge Questions:

"""
Given a list of strings representing names, write a list comprehension to create a new list containing only the names that start with a vowel (a, e, i, o, u). Additionally, transform these names to uppercase. Finally, return both the new list and the count of names in it. If no names meet the criteria, return an empty list and a count of 0.

names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]
"""
"""
1. Write a function swap_case(sentence) that takes a sentence as input and returns the sentence with swapped case (e.g., uppercase characters become 
lowercase and vice versa). For example, swap_case("Hello World") should return "hELLO wORLD"

2. Write a function count_title_case(sentence) that takes a sentence as input and returns the number of words in title case (first letter of each word capitalized). For example, count_title_case("Python is an Amazing Programming Language") should return 4.
"""