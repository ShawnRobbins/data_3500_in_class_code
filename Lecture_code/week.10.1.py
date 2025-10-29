import math
"""
Given an even number (greater than 2), return two prime numbers whoes sum will be equal to the given number.

A solution will always exist (Goldbach's Conjecture)

Example:

Input: 4
Output 2 + 2 = 4
"""

num = int(input("Please enter an even number: "))

def is_prime(num):
    is_prime = True
    if num <= 2:
        is_prime = False
    else:
        if num == 2:
            is_prime = True
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
    return is_prime


def prime_range(number):
    range_start = 0
    range_end = number + 1
    primeRange = []
    for num in range(range_start, range_end+1):
        if is_prime(num):
            primeRange.append(num)
    return primeRange


def gold_prime(primeRange, goalNum):
    for i in primeRange:
        for j in primeRange:
            if i + j == goalNum:
                return str(i) + " and " + str(j) + " are prime pairs adding up to " + str(goalNum)
            
print(gold_prime(prime_range(num), num))


# substrings
emojis = "😀😃🤣😍😎"
if "😎" in emojis:
    print("This is my favorite emoji: 😎")

# replacing
sentence = "Our offices are mainly in California but some are in New York."
sentence = sentence.replace("California", "CA")
sentence = sentence.replace("New York", "NY")
print(sentence)

# split and join
words = sentence.split(" ")
print("words", words)

text = "😎".join(words)
print("text", text)

# char test
                

