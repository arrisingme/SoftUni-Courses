fuel_type = input()
fuel_quantity = float(input())
discount_card = input()

price = 0
discount =0

if fuel_type == "Gasoline":
    price = 2.22
    if discount_card == "Yes":
        price -= 0.18
elif fuel_type == "Diesel":
    price = 2.33
    if discount_card == "Yes":
        price -= 0.12
elif fuel_type == "Gas":
    price = 0.93
    if discount_card == "Yes":
        price -= 0.08

if 20 <= fuel_quantity <= 25:
    if fuel_type == "Gasoline":
        price -= price * 0.08
    elif fuel_type == "Diesel":
        price -= price * 0.08
    elif fuel_type == "Gas":
        price -= price * 0.08
elif fuel_quantity > 25:
    if fuel_type == "Gasoline":
        price -= price * 0.10
    elif fuel_type == "Diesel":
        price -= price * 0.10
    elif fuel_type == "Gas":
        price -= price * 0.10

total_price = price * fuel_quantity

print(f"{total_price:.2f} lv.")