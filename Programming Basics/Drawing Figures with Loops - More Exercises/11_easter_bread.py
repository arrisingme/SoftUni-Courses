budget = float(input())
flour_price_per_kg = float(input())
coloured_eggs = 0

eggs_pack_of_1 = flour_price_per_kg * 0.75
milk_per_l = flour_price_per_kg * 1.25
easter_bread_price = flour_price_per_kg + eggs_pack_of_1 + (0.25 * milk_per_l)

current_bread_count = budget / easter_bread_price

print(easter_bread_price)
print(current_bread_count)