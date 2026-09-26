km_count = int(input())
time_of_the_day = input()

price = 0
starting_tax = 0

if km_count >= 100:
    price = 0.06 * km_count
elif 20 <= km_count < 100:
    price = 0.09 * km_count
elif km_count < 20:
    starting_tax = 0.70
    if time_of_the_day == "day":
        price = 0.79 * km_count
    elif time_of_the_day == "night":
        price = 0.90 * km_count

total_price = price + starting_tax

print(f"{total_price:.2f}")