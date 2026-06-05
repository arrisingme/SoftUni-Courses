from math import ceil

number_easter_bread = int(input())

total_sugar_used = 0
total_flour_used = 0
max_sugar = 0
max_flour = 0

for _ in range(number_easter_bread):
    sugar_spent = int(input())
    flour_spent = int(input())

    total_sugar_used += sugar_spent
    total_flour_used += flour_spent

    if sugar_spent > max_sugar:
        max_sugar = sugar_spent

    if flour_spent > max_flour:
        max_flour = flour_spent

total_packs_sugar_needed = ceil(total_sugar_used / 950)
total_packs_flour_needed = ceil(total_flour_used / 750)

print(f"Sugar: {total_packs_sugar_needed}")
print(f"Flour: {total_packs_flour_needed}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
