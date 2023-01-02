"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-21"
------------------------------------------------------------------------
"""

from Movie_utilities import get_by_rating, read_movies

rate = float(input("Enter a rating: "))

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = get_by_rating(movies, rate)

for i in ans:
    print(i)

fv.close()
