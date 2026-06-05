city_name = input()
sales_volume = float(input())
commission = -1

if city_name == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 <= sales_volume <= 1000:
        commission = 0.07
    elif 1000 <= sales_volume <= 10000:
        commission = 0.08
    elif sales_volume > 10000:
        commission = 0.12

elif city_name == "Varna":
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 <= sales_volume <= 1000:
        commission = 0.075
    elif 1000 <= sales_volume <= 10000:
        commission = 0.10
    elif sales_volume > 10000:
        commission = 0.13

elif city_name == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 <= sales_volume <= 1000:
        commission = 0.08
    elif 1000 <= sales_volume <= 10000:
        commission = 0.12
    elif sales_volume > 10000:
        commission = 0.145

total_commission = (sales_volume * commission)

if commission >= 0:
    print(f"{total_commission:.2f}")
else:
    print("error")

