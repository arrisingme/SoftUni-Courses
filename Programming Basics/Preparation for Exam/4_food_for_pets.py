total_days = int(input())
food_qty = float(input())

biscuits = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, total_days + 1):
    daily_food_dog = int(input())
    daily_food_cat = int(input())

    if day % 3 == 0:
        biscuits += (daily_food_dog + daily_food_cat) * 0.10

    total_dog_food += daily_food_dog
    total_cat_food += daily_food_cat

total_food = total_dog_food + total_cat_food
total_food_pct = (total_food / food_qty) * 100
dog_food_pct = (total_dog_food / total_food) * 100
cat_food_pct = (total_cat_food / total_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_pct:.2f}% of the food has been eaten.")
print(f"{dog_food_pct:.2f}% eaten from the dog.")
print(f"{cat_food_pct:.2f}% eaten from the cat.")
