'''
Creating a binary search in python.

@author: Grant Cahill
'''

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    iteration = 0
    previous_index = 0
    index = len(input_array)/2
    while index < len(input_array):
        iteration += 1
        # Check for value
        if input_array[index] == value:
            return index
        # Check to see if we overshot the value
        elif input_array[index] > value:
            if (index - 1) == previous_index:
                return -1
            else:
                if previous_index == 0:
                    index = previous_index + (index/2)
                else:
                    index = previous_index + (index/previous_index)
        # Keep halving and incrementing
        else:
            if (index+1) == len(input_array):
                return -1
            previous_index = index
            increment = (len(input_array) - index)/2
            index += increment

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)