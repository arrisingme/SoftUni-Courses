budget = float(input())
category = input()
people = int(input())

if 1 <= people <= 4:
    transport_costs = (budget * 0.75)
elif 5 <= people <= 9:
    transport_costs = (budget * 0.60)
elif 10 <= people <= 24:
    transport_costs = (budget * 0.50)
elif 25 <= people <= 49:
    transport_costs = (budget * 0.40)
else:
    transport_costs = (budget * 0.25)
if category == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99

remaining_budget = (budget - transport_costs)
total_tickets_cost = (people * ticket_price)
diff = abs(remaining_budget - total_tickets_cost)

if remaining_budget >= total_tickets_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")