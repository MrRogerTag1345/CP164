"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-10-28"
------------------------------------------------------------------------
"""

from List_array import List

l = [11, 22, 33, 44, 55, 55]
target = [11, 22, 33, 44, 55]
s = List()

for i in l:
    s.append(i)

print(s.is_identical(target))
print(s.remove_many(55))
    
