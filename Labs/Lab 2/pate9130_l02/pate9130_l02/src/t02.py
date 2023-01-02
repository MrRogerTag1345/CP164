"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-24"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array, array_to_stack

s = Stack()
l = [0, 1, 2, 3, 4, 5]

temp = array_to_stack(s, l)

'''
This only works when something is returned
for i in temp:
    print(i)
'''
