budget = float(input())
actors = int(input())
clothing_price = float(input())

decor = budget * 0.10

if actors > 150:
    clothing_price = clothing_price * 0.90

total_clothing_expense = actors * clothing_price
total_expense = (total_clothing_expense + decor)

if total_expense > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(total_expense - budget):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {(budget - total_expense):.2f} leva left.")