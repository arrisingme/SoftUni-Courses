years = int(input())
washer_price = float(input())
toy_price = int(input())

savings = 0
coefficient = 1

for i in range(1, years + 1):
    if i % 2 != 0:
        savings += toy_price
    elif i % 2 == 0:
        savings += coefficient * 10
        savings -= 1
        coefficient += 1
if savings >= washer_price:
    print(f"Yes! {(savings - washer_price):.2f}")
else:
    print(f"No! {(washer_price - savings):.2f}")

