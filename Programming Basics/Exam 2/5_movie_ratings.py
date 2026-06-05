from sys import maxsize

number_wanted_movies = int(input())

max_rating = - maxsize
min_rating = maxsize
total_rating = 0
highest_movie_rating = 0
lowest_movie_rating = 0

for _ in range(number_wanted_movies):
    name_of_movie = input()
    rating = float(input())

    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        highest_movie_rating = name_of_movie
    elif rating < min_rating:
        min_rating = rating
        lowest_movie_rating = name_of_movie

avg_rating = total_rating / number_wanted_movies

print(f"{highest_movie_rating} is with highest rating: {max_rating}")
print(f"{lowest_movie_rating} is with lowest rating: {min_rating}")
print(f"Average rating: {avg_rating:.1f}")