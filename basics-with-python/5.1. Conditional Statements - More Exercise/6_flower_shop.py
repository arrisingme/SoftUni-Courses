from math import ceil

q_magnolias = int(input())
q_hyacinths = int(input())
q_roses = int(input())
q_cactus = int(input())
gift_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cactus_price = 8

total_magnolias_price = q_magnolias * magnolias_price
total_hyacinths_price = q_hyacinths * hyacinths_price
total_roses_price = q_roses * roses_price
total_cactus_price = q_cactus * cactus_price

total_profit = (total_magnolias_price + total_hyacinths_price
                + total_roses_price + total_cactus_price)
total_profit *= 0.95

if total_profit >= gift_price:
    print(f"She is left with {int(total_profit - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - total_profit)} leva.")