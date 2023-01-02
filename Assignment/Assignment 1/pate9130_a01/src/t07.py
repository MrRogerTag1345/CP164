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

from functions import file_analyze

fv = open("text.txt", "r")

u, l, d, w, r = file_analyze(fv)

print ("There are {} upper case letters".format(u))
print ("There are {} lower case letters".format(l))
print ("There are {} digits".format(d))
print ("There are {} white spaces".format(w))
print ("There are {} characters".format(r))
