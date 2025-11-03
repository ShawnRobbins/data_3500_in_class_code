"""
Write a python function that takes a strings as input and checks
if it is a palindrom (reads the same backward as forward).
Ignore spaces, punctuation, and consider case-insensititve matches
"""

def pal_checker(string):
    clean_str = ""
    # for char in string:
    #     if char.isalpha():
    #         clean_str += char.lower()
    clean_str = "".join(char.lower() for char in string if char.isalpha())
    return clean_str == clean_str[::-1]

strings_to_test = [
    "Sit on a potato pan, Otis.",
    "Cigar? Toss it in a can. It is so tragic.",
    "Go hang a salami, I'm a lasagna hog.",
    "A man, a plan, a canal, Panama!",
    "Aggie basketball starts tonight and I am so excited!"
]

for string in strings_to_test:
    if pal_checker(string):
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")