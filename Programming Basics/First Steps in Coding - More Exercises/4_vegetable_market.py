veg_price_kg = float(input())
fruit_price_kg = float(input())
veg_quantity = int(input())
fruit_quantity = int(input())

eur = 1.94

total_veg_sold = (veg_price_kg * veg_quantity)
total_fruit_sold = (fruit_price_kg * fruit_quantity)

total_quantity_sold = (total_veg_sold + total_fruit_sold) / eur

total_quantity_sold = f"{total_quantity_sold:.2f}"

print(total_quantity_sold)