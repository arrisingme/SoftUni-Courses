import math
from math import floor, ceil

racket_price = float(input())
number_tennis_rackets = int(input())
number_pair_trainers = int(input())

total_racket_price = racket_price * number_tennis_rackets
total_trainers_price = (1 / 6 * racket_price) * number_pair_trainers
total_equipment = (total_racket_price + total_trainers_price) * 0.20
total_amount = (total_racket_price + total_trainers_price + total_equipment)

djokovic_price = math.floor(1 / 8 * total_amount)
sponsor_price = math.ceil(7 / 8 * total_amount)

print(f"Price to be paid by Djokovic {djokovic_price}")
print(f"Price to be paid by sponsors {sponsor_price}")