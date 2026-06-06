pct_fat = int(input())
pct_protein = int(input())
pct_carbochidrates = int(input())
total_calorie = int(input())
pct_water = int(input())

total_grams_fat = (pct_fat * total_calorie) / 100 / 9
total_grams_protein = (pct_protein * total_calorie) / 100 / 4
total_grams_carbochidrates = (pct_carbochidrates * total_calorie) / 100 / 4
calorie_per_gram_food = (total_calorie / (total_grams_fat + total_grams_protein + total_grams_carbochidrates))
calorie_without_water = (calorie_per_gram_food * (100 - pct_water)) / 100

print(f"{calorie_without_water:.4f}")
