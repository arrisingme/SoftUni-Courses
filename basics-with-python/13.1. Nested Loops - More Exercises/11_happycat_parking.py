day_count = int(input())
hours_per_day_count = int(input())

price = 0
total_sum = 0

for i in range(1, day_count + 1):
    total_per_day = 0
    for j in range(1, hours_per_day_count + 1):
        if i % 2 == 0 and j % 2 != 0:
            price = 2.50
        elif i % 2 != 0 and j % 2 == 0:
            price = 1.25
        else:
            price = 1.00
        total_per_day += price
    total_sum += total_per_day
    print(f"Day: {i} - {total_per_day:.2f} leva")

print(f"Total: {total_sum:.2f} leva")
