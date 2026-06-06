type = input()
rows = int(input())
colomns = int(input())
income = 0

price_premiere = 12
price_normal = 7.5
price_discount = 5

capacity = (rows * colomns)

if type == "Premiere":
    income = (price_premiere * capacity)
elif type == "Normal":
    income = (price_normal * capacity)
elif type == "Discount":
    income = (price_discount * capacity)

print(f"{income:.2f} leva")