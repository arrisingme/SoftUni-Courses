budget = float(input())
nights_stays = int(input())
price_per_night = float(input())
additional_costs = int(input())

if nights_stays > 7:
    discount = price_per_night * 0.05
    price_per_night -= discount

needed_money = (nights_stays * price_per_night) + ((budget * additional_costs) / 100)

if budget >= needed_money:
    print(f"Ivanovi will be left with {(budget - needed_money):.2f} leva after vacation.")
else:
    print(f"{(needed_money -budget):.2f} leva needed.")

