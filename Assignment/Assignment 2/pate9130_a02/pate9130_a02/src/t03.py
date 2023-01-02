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

from Movie_utilities import get_by_genre, read_movies

genre = int(input("Enter a genre: "))

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = get_by_genre(movies, genre)
fv.close()

for i in ans:
    print(i)
