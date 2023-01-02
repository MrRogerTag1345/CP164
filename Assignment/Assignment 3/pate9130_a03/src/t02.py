"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-29"
------------------------------------------------------------------------
"""

from Stack_array import Stack

s = Stack()
# l = [8, 14, 12, 9, 8, 7, 5]
l = [0, 1]

for i in l:
    s.push(i)

t1, t2 = s.split_alt()

for i in t1:
    print(i)
    
print("*"*60)

for i in t2:
    print(i)
