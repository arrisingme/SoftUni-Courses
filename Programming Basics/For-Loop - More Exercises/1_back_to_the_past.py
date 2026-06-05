heritage_money = float(input())
year_to_live_to = int(input())

years_old = 18
expenses = 0
year = 0

for year in range (1800, year_to_live_to +1, 1):
    if year % 2 == 0:
        expenses += 12000
    else:
        expenses += (12000 + 50 * years_old)
    years_old += 1
money_left = (heritage_money - expenses)

if heritage_money >= expenses:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {(expenses - heritage_money):.2f} dollars to survive.")

