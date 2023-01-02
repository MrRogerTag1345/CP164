"""
------------------------------------------------------------------------
t01.py
Program Determins if the year is leap or not.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-08"
------------------------------------------------------------------------
"""

# Import.
from functions import is_leap_year

# User input.
year = int(input("Enter a Year: "))

# Send Results to function.
leap_year = is_leap_year(year)

# Result.
if leap_year == True:
    print("{}".format(leap_year))
else:
    print("{}".format(leap_year))
