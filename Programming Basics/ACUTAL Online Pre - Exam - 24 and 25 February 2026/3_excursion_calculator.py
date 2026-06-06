people_number = int(input())
season = input()

price = 0

if people_number <= 5:
    if season == "spring":
        price = 50.00
    elif season == "summer":
        price = 48.50 * 0.85
    elif season == "autumn":
        price = 60.00
    elif season == "winter":
        price = 86.00 * 1.08

elif people_number > 5:
    if season == "spring":
        price = 48.00
    elif season == "summer":
        price = 45.00 * 0.85
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85.00 * 1.08

total_price = price * people_number

print(f"{total_price:.2f} leva.")

