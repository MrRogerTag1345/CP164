"""
------------------------------------------------------------------------
t02.py
This is a program that determines the smallest, largest, total, and average
values in a list. 
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-16"
------------------------------------------------------------------------
"""

# Import.
from functions import list_stats

# Hard list.    
l = [20, 5000, 75.1, 10, 3, -11]

# Function input.
small, large, total, average = list_stats(l)

# Print Statement.
print("Smallest Value: {}".format(small))
print("Largest Value: {}".format(large))
print("Total Value: {}".format(total))
print("Average Value: {:2f}".format(average))

