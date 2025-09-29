'''
Given a list of integers, return a new list such that each element at the index of i of the new list is the product of all the numbers in the orignal list except for the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

input_list = [1, 2, 3, 4, 5]
output_list = []



for i in input_list:
    product = 1
    for j in input_list:
        if i == j:
            continue
        product *= j
    
    output_list.append(product)

print("output list:", output_list)

print(input_list)

# lists

ages = [22, 34, 98, 67]
ages.append(21)
print("ages:", ages)
ages.pop()
print("ages:", ages)
ages.pop(2)
print("ages:", ages)
ages.insert(2, 101)
print("ages:", ages)

# if two words are anagrams

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word1_list = []
for letter in word1:
    word1_list.append(letter)

word2_list = []
for letter in word2:
    word2_list.append(letter)

word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print("These words are anagrams")
else:
    print("These words are not anagrams")

