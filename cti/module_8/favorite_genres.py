
'''
Congratulations on your new job as Chief Algorithm Developer at a new small startup called WebFilms. Your job is to find a group of users' favorite movie genre. You're given:

    A list of users, by ID
    A list of movie IDs, with their rating (a number, 1-5), and which userID gave that rating
    A list of movies, by ID, with their genres attached


The Users array will have multiple elements that look like this:

users = [{'id': "923874rksd9293"}]



The movie ratings array will have multiple elements that look like this:

movie_ratings = [
  {
    'movie_id': "20jfcf02341kwd",
    'user_id': "923874rksd9293", 
    'rating': 5
  }
]



The movies array will have multiple elements that look like this:

movies = [
  {
     "id": "20jfcf02341kwd",
     "genre": "animated"
  }
]


In order to simplify the problem, Movies will always have a single genre, all movies from the movie_ratings list will be in the movies list, and all users from the movie_ratings list will be in the users list.

Return a list of users, with their favorite genre. "Favorite Genre" means the genre with the highest average rating. If there are multiple, return the first one you find with a perfect 5.0.

users = [
  {
    "id": "923874rksd9293",
    "favorite_genre": "animated"
  }
]



** scratch paper **

See module_8 Jupyter notebook.



** pseudocode **


create list of {users : favorite_genre}
for each user:

    create a list of their { movies : score }

    # create_genre_counts()
    make an empty {genre : [total, counts]} list
    for each {movies : score}:
        find movie genre
        add movie score to total for that genre
        tally counts of scores for that genre
        add to {genre : [total, counts]}

    # calculate_average()
    for each {genre : [total, counts]}:
        average = total / counts
        add to {genre : [total, counts, average]}

    # create_favorite_list()
    create largest_average = {genre : average}
    for each average:
        if larger than largest_average, reassign variable
    save to {users : favorite_genre}
        
    




'''


def favorite_genres(users, movies, movie_ratings):
    '''
    Make a list of favorite movie genres from a list of users and
    records of their ratings of some movies.
    '''
    # create list of {users : favorite_genre}
    users_favorites = []
    # for each user:
    movies_length = len(movies)
    for user in users:
    #     create a list of their { movies : score }

        users_ratings = create_users_ratings(user, movie_ratings)
        genre_scores = aggregate_users_ratings(users_ratings, movies)
        favorite = find_favorite(genre_scores)
        append_favorite(user, favorite, users_favorites)

    return users_favorites





def create_users_ratings(user, movie_ratings):
    '''Return a dictionary with a particular user's movie ratings.'''
    users_movies = {}
    for movie in movie_ratings:
        # print(user['id'])
        # print(movie)
        # print(type(movie))
        # print(movie['user_id'])
        if user['id'] == movie['user_id']:
            if movie['movie_id'] not in users_movies:
                users_movies[movie['movie_id']] = movie['rating']

    return users_movies


def aggregate_users_ratings(users_ratings, movies):
    ''' 
    Return a dictionary with genres as keys and a list with 
    the sum and counts of the ratings.
    '''
    movies_length = len(movies)
    # print(movies_length)
    genre_scores = {}
    for key in users_ratings:
        # print(key)
        found = False
        index = 0
        while not found and index < movies_length:
            if key == movies[index]['id']:
                found = True
                # print(found)
                # print(key)
                if movies[index]['genre'] not in genre_scores:
                    genre_scores[movies[index]['genre']] = [users_ratings[key], 1]
                    # print(genre_scores)
                else:
                    genre_scores[movies[index]['genre']][0] += users_ratings[key]
                    genre_scores[movies[index]['genre']][1] += 1
            else:
                index += 1
                # print(found)
    
    return genre_scores


def find_favorite(genre_scores):
    '''Return the favorite genre of a user.'''
    high_score = 0
    favorite = ''
    for key in genre_scores:
        average = genre_scores[key][0] / genre_scores[key][1]
        if average > high_score:
            high_score = average
            favorite = key

    return favorite



def append_favorite(user, favorite, users_favorites):
    '''Append a dictionary with user id and favorite to a list.'''
    high_score = 0
    user_fave = {'id': user['id'], 'favorite_genre': favorite}
    users_favorites.append(user_fave)





if __name__ == '__main__':
    users = [{'id': "923874rksd9293"}]
    movie_ratings = [
  {
    'movie_id': "20jfcf02341kwd",
    'user_id': "923874rksd9293", 
    'rating': 5
  }
]
    movies = [
  {
     "id": "20jfcf02341kwd",
     "genre": "animated"
  }
]

    print(favorite_genres(users, movies, movie_ratings))
