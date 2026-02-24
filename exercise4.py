def recommened_movies(movie_list):
    count=0
    for i in movie_list:
        if i['genre'].lower()=='action' and i['rating']>=8.0:
            print(f"Watch {i['title']}, it is great movie")
            count+=1
    if count==0:
        print("The list is not good")        
movies = [
    {'title': 'Mad Max', 'genre': 'Action', 'rating': 8.5},
    {'title': 'Titanic', 'genre': 'Romance', 'rating': 9.0},
    {'title': 'John Wick', 'genre': 'Action', 'rating': 8.0},
    {'title': 'Fast X', 'genre': 'Action', 'rating': 6.5}
]
recommened_movies(movies)