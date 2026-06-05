budget = float(input())
season = input()

location = 0
type_of_stay = 0

if season == "Summer" and budget <= 1000:
    type_of_stay = "Camp"
    location = "Alaska"
    price = budget * 0.65
elif season == "Summer" and 1000 < budget <= 3000:
    type_of_stay = "Hut"
    location = "Alaska"
    price = budget * 0.80
elif season == "Summer" and budget > 3000:
    type_of_stay = "Hotel"
    location = "Alaska"
    price = budget * 0.90
elif season == "Winter" and budget <= 1000:
    type_of_stay = "Camp"
    location = "Morocco"
    price = budget * 0.45
elif season == "Winter" and 1000 < budget <= 3000:
    type_of_stay = "Hut"
    location = "Morocco"
    price = budget * 0.60
elif season == "Winter" and budget > 3000:
    type_of_stay = "Hotel"
    location = "Morocco"
    price = budget * 0.90

print(f"{location} - {type_of_stay} - {price:.2f}")