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
l = [8, 14, 12, 9, 8, 7, 5]

for i in l:
    s.push(i)
    
for j in s:
    print(j)
    
print("*"*60)
    
ans = s.reverse()

for i in ans:
    print(i)
