budget = float(input())
season = input()

class_type = 0
price = 0
car_type = 0

if season == "Summer" and budget <= 100:
    class_type = "Economy class"
    car_type = "Cabrio"
    price = budget * 0.35
elif season == "Summer" and 100 < budget <= 500:
    class_type = "Compact class"
    car_type = "Cabrio"
    price = budget * 0.45

if season == "Winter" and budget <= 100:
    class_type = "Economy class"
    car_type = "Jeep"
    price = budget * 0.65
elif season == "Winter" and 100 < budget <= 500:
    class_type = "Compact class"
    car_type = "Jeep"
    price = budget * 0.80

elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90

print(class_type)
print(f"{car_type} - {price:.2f}")