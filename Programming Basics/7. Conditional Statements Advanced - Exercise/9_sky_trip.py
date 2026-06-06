days_stay = int(input())
room_type = input()
rating = input()

total_price = 0
nights_stay = (days_stay - 1)

room_for_one_person_per_night = 18.00
apartment_per_night = 25.00
president_apartment_per_night = 35.00

if room_type == "room for one person":
    total_price = (nights_stay * room_for_one_person_per_night)

elif room_type == "apartment":
    total_price = (nights_stay * apartment_per_night)
    if days_stay < 10:
       total_price *= 0.70
    elif 10 <= days_stay <= 15:
        total_price *= 0.65
    elif days_stay > 15:
        total_price *= 0.50

elif room_type == "president apartment":
    total_price = (nights_stay * president_apartment_per_night)
    if days_stay < 10:
       total_price *= 0.90
    elif 10 <= days_stay <= 15:
        total_price *= 0.85
    elif days_stay > 15:
        total_price *= 0.80

if rating == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

print(f"{total_price:.2f}")