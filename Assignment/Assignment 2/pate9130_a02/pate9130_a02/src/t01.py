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

from Movie_utilities import get_by_year, read_movies

# Test using 2007
year = int(input("Enter a year for movie: "))

fv = open("movies.txt", "r")

movies = read_movies(fv)
ans = get_by_year(movies, year)

for i in ans:
    print(i)

fv.close()

