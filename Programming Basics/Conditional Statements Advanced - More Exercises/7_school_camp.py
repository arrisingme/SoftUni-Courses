season = input()
group_type = input()
students_number = int(input())
nights = int(input())

sport = 0
price = 0
discount = 0

if season == "Winter":
    if group_type == "boys":
        price = 9.60
        sport = "Judo"
    elif group_type == "girls":
        price = 9.60
        sport = "Gymnastics"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = 7.20
        sport = "Tennis"
    elif group_type == "girls":
        price = 7.20
        sport = "Athletics"
    elif group_type == "mixed":
        price = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"

total_price = price * students_number * nights

if students_number >= 50:
    discount = total_price * 0.50
    total_price -= discount
elif 20 <= students_number < 50:
    discount = total_price * 0.15
    total_price -= discount
elif 10 <= students_number < 20:
    discount = total_price * 0.05
    total_price -= discount



print(f"{sport} {total_price:.2f} lv.")

