movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

price_per_day = 0

if season == "Windet":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    elif destination == "London":
        price_per_day = 24000

elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    elif destination == "London":
        price_per_day = 20250

total_price = number_of_days * price_per_day

if destination == "Dubai":
    total_price *= 0.70
elif destination == "Sofia":
    total_price *= 1.25

if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {(movie_budget - total_price):.2f} leva left!")
else:
    print(f"The director needs {(total_price - movie_budget):.2f} leva more!")