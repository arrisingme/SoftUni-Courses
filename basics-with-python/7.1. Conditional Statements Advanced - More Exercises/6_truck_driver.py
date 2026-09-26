season = input()
km_per_month = float(input())

price_per_km = 0
whole_season = 4

if season == "Spring" or season == "Autumn" and km_per_month <= 5000:
    price_per_km = 0.75
elif season == "Spring" or season == "Autumn" and 5000 < km_per_month <= 10000:
    price_per_km = 0.95
elif season == "Summer" and km_per_month <= 5000:
    price_per_km = 0.90
elif season == "Summer" and 5000 < km_per_month <= 10000:
    price_per_km = 1.10
elif season == "Winter" and km_per_month <= 5000:
    price_per_km = 1.05
elif season == "Winter" and 5000 < km_per_month <= 10000:
    price_per_km = 1.25

if 10000 < km_per_month <= 20000:
    price_per_km = 1.45

total_salary = (price_per_km * km_per_month * whole_season)
total_salary -= total_salary * 0.10

print(f"{total_salary:.2f}")