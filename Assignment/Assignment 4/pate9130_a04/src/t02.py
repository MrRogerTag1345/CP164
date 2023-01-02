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

LINE = "*"*60

from Queue_array import Queue
from functions import queue_combine
from utilities import array_to_queue

q1 = Queue()
q2 = Queue()

l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

array_to_queue(q1, l2)
array_to_queue(q2, l)

'''
for i in l:
    q1.insert(i)
    
for j in l2:
    q2.insert(j)
'''
  
ans = queue_combine(q1, q2)

# print(LINE)

while not ans.is_empty():
    print(ans.remove())

