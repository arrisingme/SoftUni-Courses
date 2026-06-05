months = int(input())

expense_water = 20
expense_internet = 15
total_electricity_expense = 0
total_water_expense = 0
total_internet_expense = 0
total_expense_other = 0
total_amount = 0
avg = 0

for i in range(months):
    electricity_expense_a_month = float(input())

    total_electricity_expense += electricity_expense_a_month
    total_water_expense += expense_water
    total_internet_expense += expense_internet
    total_expense_other += (expense_water + expense_internet + electricity_expense_a_month) * 1.20
    total_amount = (total_electricity_expense + total_water_expense + total_internet_expense + total_expense_other)
    avg = total_amount / months

print(f"Electricity: {total_electricity_expense:.2f} lv")
print(f"Water: {total_water_expense:.2f} lv")
print(f"Internet: {total_internet_expense:.2f} lv")
print(f"Other: {total_expense_other:.2f} lv")
print(f"Average: {avg:.2f} lv")
