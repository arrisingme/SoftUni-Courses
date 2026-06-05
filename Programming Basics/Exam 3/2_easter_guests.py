from math import ceil

guests_number = int(input())
budget = int(input())

easter_bread_price = 4
egg_price = 0.45

easter_bread_per_person = ceil(guests_number / 3)
eggs_per_person = ceil(guests_number * 2)

total_easter_bread = easter_bread_per_person * easter_bread_price
total_eggs = eggs_per_person * egg_price
total_amount = (total_easter_bread + total_eggs)

if budget >= total_amount:
    print(f"Lyubo bought {easter_bread_per_person} Easter bread and {eggs_per_person} eggs.")
    print(f"He has {(budget - total_amount):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {(total_amount - budget):.2f} lv. more.")