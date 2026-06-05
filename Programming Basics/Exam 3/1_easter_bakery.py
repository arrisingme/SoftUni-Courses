flour_kg_price = float(input())
flour_quantity_kg = float(input())
sugar_quantity_kg = float(input())
boxes_of_eggs = int(input())
yeast_quantity = int(input())

sugar_kg_price = flour_kg_price * 0.75
boxes_of_eggs_price = flour_kg_price * 1.10
yeast_price = sugar_kg_price * 0.20

total_flour_amount = flour_quantity_kg * flour_kg_price
total_sugar_amount = sugar_quantity_kg * sugar_kg_price
total_eggs_amount = boxes_of_eggs * boxes_of_eggs_price
total_yeast_amount = yeast_quantity * yeast_price

total_expense = (total_flour_amount + total_sugar_amount + total_eggs_amount
                 + total_yeast_amount)

print(f"{total_expense:.2f}")