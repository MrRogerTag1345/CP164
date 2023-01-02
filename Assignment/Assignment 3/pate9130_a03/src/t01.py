"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-30"
------------------------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_split_alt

s = Stack()
l = [5, 7, 8, 9, 12, 14, 8]

for i in l:
    s.push(i)
    
a1, a2 = stack_split_alt(s)

for i in a1:
    print(i)
    
print("*"*60)

for i in a2:
    print(i)
