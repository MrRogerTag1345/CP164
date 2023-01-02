"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-10-07"
------------------------------------------------------------------------
"""

from Queue_circular import Queue

q = Queue()
l = [1, 2, 3, 4, 5]

for i in l:
    q.insert(i)
    
print(q.peek())
print(q.is_empty())
print(q.is_full())

while not q.is_empty():
    print(q.remove())
    
