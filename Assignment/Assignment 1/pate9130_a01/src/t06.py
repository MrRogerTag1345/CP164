"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-16"
------------------------------------------------------------------------
"""

from functions import matrix_stats

a = [[1, 2, -35], [10, 15, 20, -1], [2, 30]]

small, large, total, average = matrix_stats(a)

# Print Statement.
print("Smallest Value: {}".format(small))
print("Largest Value: {}".format(large))
print("Total Value: {}".format(total))
print("Average Value: {:2f}".format(average))
