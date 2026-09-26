from math import floor, ceil

vine_sq_space = int(input())
kg_grapes_per_sq_m = float(input())
needed_liters = int(input())
workers_number = int(input())

liter = kg_grapes_per_sq_m / 2.50
allocated = vine_sq_space * 0.40
produced_wine = allocated * liter
wine_per_worker = (produced_wine - needed_liters) / workers_number

if produced_wine < needed_liters:
    print(f"It will be a tough winter! More {floor(needed_liters - produced_wine)} liters wine needed.")
elif produced_wine >= needed_liters:
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    print(f"{ceil(produced_wine - needed_liters)} liters left -> {ceil(wine_per_worker)} liters per person.")