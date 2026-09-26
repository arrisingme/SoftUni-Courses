from math import floor, ceil

days = int(input())
kg_food_left = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

total_food_dog = food_for_dog * days
total_food_cat = food_for_cat * days
total_food_turtle = (food_for_turtle * days) / 1000

total_food_for_pets = (total_food_dog + total_food_cat + total_food_turtle)

if kg_food_left >= total_food_for_pets:
    print(f"{floor(kg_food_left - total_food_for_pets)} kilos of food left.")
else:
    print(f"{ceil(total_food_for_pets - kg_food_left)} more kilos of food are needed.")