kozunak_number = int(input())
box_of_eggs_number = int(input())
cookies_kg= int(input())

kozunak_price = 3.20
box_of_eggs_price = 4.35
cookie_kg_price = 5.40
paint_for_eggs = 0.15

total_expense_kozunak = kozunak_number * kozunak_price
total_expense_box_of_eggs = box_of_eggs_number * box_of_eggs_price
total_expense_cookie = cookies_kg * cookie_kg_price
total_expense_paint_for_eggs = 12 * box_of_eggs_number * paint_for_eggs

total_expense = (total_expense_kozunak + total_expense_box_of_eggs + total_expense_cookie + total_expense_paint_for_eggs)

print(f"{total_expense:.2f}")