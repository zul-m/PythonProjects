from imdb import IMDb

# Searching for a movie with random id.
movie = IMDb().get_movie('012345')
print("Movie name:", movie)

# Directors of the movie.
for i in movie["directors"]:
    print("Directors:", i)

print("\n******************** Top 250 Movies ********************\n")
# Look at the top 250 movies in IMDb.
movies = IMDb().get_top250_movies()
for i in movies:
    print(i)