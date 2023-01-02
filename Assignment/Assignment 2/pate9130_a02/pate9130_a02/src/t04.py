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

from Movie_utilities import get_by_genres, read_movies

genres = [3, 4]

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = get_by_genres(movies, genres)

for i in ans:
    print(i)

fv.close()
