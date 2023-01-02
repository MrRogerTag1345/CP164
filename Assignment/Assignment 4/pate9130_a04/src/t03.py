"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-10-05"
------------------------------------------------------------------------
"""

from Queue_array import Queue
from utilities import array_to_queue

ans = Queue()

q1 = Queue()
q2 = Queue()

l = [2, 5, 1, 5, 237, 25, 72, 46]
l2 = [36, 123, 7, 34, 7, 12, 37, 3, 47, 2]

array_to_queue(q1, l)
array_to_queue(q2, l2)

ans.combine(q1, q2)

while not ans.is_empty():
    print(ans.remove())
