flower_type = (input())
total_flowers = int(input())
budget = int(input())
total_amount = 0

rose_price = 5
dahlia_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flower_type == "Roses":
    total_amount = (rose_price * total_flowers)
    if total_flowers > 80:
        total_amount *= 0.90
elif flower_type == "Dahlias":
    total_amount = (dahlia_price * total_flowers)
    if total_flowers > 90:
        total_amount *= 0.85
elif flower_type == "Tulips":
    total_amount = (tulips_price * total_flowers)
    if total_flowers > 80:
        total_amount *= 0.85
elif flower_type == "Narcissus":
    total_amount = (narcissus_price * total_flowers)
    if total_flowers < 120:
        total_amount *= 1.15
elif flower_type == "Gladiolus":
    total_amount = (gladiolus_price * total_flowers)
    if total_flowers < 80:
        total_amount *= 1.20
if budget >= total_amount:
    print(f"Hey, you have a great garden with {total_flowers} {flower_type} and {(budget - total_amount):.2f} leva left.")
else:
    print(F"Not enough money, you need {(total_amount- budget):.2f} leva more.")