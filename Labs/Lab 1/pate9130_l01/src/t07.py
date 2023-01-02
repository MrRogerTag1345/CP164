"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-17"
------------------------------------------------------------------------
"""

from Movie_utilities import read_movies

fv = open("movies.txt", "r")

print("{}".format(read_movies(fv)))

fv.close()
