
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


** pseudocode **


create list of {users : favorite_genre}
for each user:
    create a list of their { movies : score }
    make an empty {genre : [total, counts]} list
    for each {movies : score}:
        find movie genre
        add movie score to total for that genre
        tally counts of scores for that genre
        add to {genre : [total, counts]}
    for each {genre : [total, counts]}:
        average = total / counts
        add to {genre : [total, counts, average]}
    create largest_average = {genre : average}
    for each average:
        if larger than largest_average, reassign variable
    save to {users : favorite_genre}
        
    




'''

from collections import Counter

def favorite_genres(users, movies, movie_ratings):

    # create list of {users : favorite_genre}
    users_favorites = []
    # for each user:
    movies_length = len(movies)
    for user in users:
    #     create a list of their { movies : score }
        users_movies = []
        for movie in movie_ratings:
            if user['id'] = movie['user_id']:
                
                ## TODO : THIS DICTIONARY MUST APPEAR IN FORMAT:
                ## {'movie_id': 12345, 'rating': 100}
                users_movies.append({movie['movie_id'] : movie['rating']})

    #     make an empty {genre : [total, counts]} list
        genre_scores = Counter()
    #     for each {movies : score}:
        for user_movie in users_movies:
    #         find movie genre
            found = False
            index = 0
            while not found or index == movies_length:
                if movies[index]['id'] == user_movie['movie_id']
                    genre = movies[index]['genre']
                    found = True
                else:
                    index += 1
            
    #         add movie score to total for that genre
            genre_scores[genre] += 
    #         tally counts of scores for that genre
    #         add to {genre : [total, counts]}
    #     for each {genre : [total, counts]}:
    #         average = total / counts
    #         add to {genre : [total, counts, average]}
    #     create largest_average = {genre : average}
    #     for each average:
    #         if larger than largest_average, reassign variable
    #     save to {users : favorite_genre}



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

    favorite_genres(users, movies, movie_ratings)
