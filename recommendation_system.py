


def show_predictions(input):
    import numpy as np
    import pandas as pd
    # load datasets
    ratings_data = pd.read_csv("ml-latest-small\\ratings.csv")
    movie_names = pd.read_csv("ml-latest-small\\movies.csv")
    # merge the two datasets
    movie_data = pd.merge(ratings_data, movie_names, on='movieId')
    # add mean rating for every movie and group by title
    ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())

    # count the total number of ratings and add them to the dataset
    ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())

    # we create a matrix of users as rows and movies as columns with cells as the rating for a particular movie
    # by a particular user
    user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')

    # we find the rating for the movie given by the users and then we corelate it with every other movie in the dataset
    movie_rating = user_movie_rating[input]
    movies_like_input = user_movie_rating.corrwith(movie_rating)

    # we add a column in the dataset to represent the correlation
    corr_movie = pd.DataFrame(movies_like_input, columns=['Correlation'])

    # we drop the users who didn't give a rating and sort the table
    corr_movie.dropna(inplace=True)
    corr_movie.sort_values('Correlation', ascending=False)

    # we join the ratings_count column from the original dataset
    corr_movie = corr_movie.join(ratings_mean_count['rating_counts'])

    # display the movies with more than 50 votes and highest correlation
    print(corr_movie[corr_movie['rating_counts'] > 50].sort_values('Correlation', ascending=False).head())
