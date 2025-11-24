"""
Write a function taht will, given a sorted listed of integers, square the elements and give the output in sorted order.
for example give [-9, -2, 0 , 2, 3] return [0, 4, 4, 9, 81]
"""

def square_sort(list):
    squared_list = [item**2 for item in list]
    squared_list.sort()
    return squared_list

print(square_sort([-9, -2, 0 , 2, 3]))
    