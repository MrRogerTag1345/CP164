"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-23"
------------------------------------------------------------------------
"""

from Movie_utilities import genre_counts, read_movies

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = genre_counts(movies)

print(ans)
