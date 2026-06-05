destination = input()

min_budget = float(input())

savings_money = 0

while savings_money < min_budget:
    savings = float(input())
    savings_money += savings

print(f"Going to {destination}!")
destination = input()
