"""
------------------------------------------------------------------------
t05.py

------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-13"
------------------------------------------------------------------------
"""

# Import function.
from functions import matrix_transpose

# Hard List.
a = [[0, 1, 2], [2, 3, 4]]

ans = matrix_transpose(a)

for i in ans:
    print("{}".format(i))
