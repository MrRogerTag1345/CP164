"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-24"
------------------------------------------------------------------------
"""

from utilities import stack_test

fv = open("movies.txt", "r")
l = []

for line in fv:
    l.append(line)

stack_test(l)

fv.close()
