n_years = int(input())
x_washer_price = float(input())
p_toy_price = int(input())

savings = 0
coefficient = 1


for i in range(1, n_years + 1, ):
    if i % 2 != 0:
        savings += p_toy_price
    elif i % 2 == 0:
        savings += (coefficient * 10)
        savings -= 1
        coefficient += 1
if savings >= x_washer_price:
    print(f"Yes! {(savings - x_washer_price):.2f}")
else:
    print(f"No! {(x_washer_price - savings):.2f}")



