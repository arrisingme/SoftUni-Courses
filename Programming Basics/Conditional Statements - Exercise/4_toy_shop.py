price_for_trip = float(input())
total_puzzles = int(input())
total_dolls = int(input())
total_bears = int(input())
total_minions = int(input())
total_trucks = int(input())

price_puzzle = 2.60
price_dolls = 3
price_bears = 4.10
price_minions = 8.20
price_trucks = 2

total_price = (total_puzzles * price_puzzle) + \
              (total_dolls * price_dolls) + \
              (total_bears * price_bears) + \
              (total_minions * price_minions) + \
              (total_trucks * price_trucks)

total_toys = (total_puzzles + total_dolls + total_bears + total_minions + total_trucks)

if total_toys >= 50:
    discount = total_price * 0.25
    total_price -= discount

rent = total_price * 0.10
total_price -= rent

if price_for_trip <= total_price:
    print(f"Yes! {total_price - price_for_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_for_trip - total_price:.2f} lv needed.")