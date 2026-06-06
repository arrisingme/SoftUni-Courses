money_allowance = float(input())
money_from_sale = float(input())
expenses_whole_period = float(input())
gift_price = float(input())

total_money = money_allowance * 5
total_money_from_sale = money_from_sale * 5
total_amount = (total_money + total_money_from_sale) - expenses_whole_period

if total_amount > gift_price:
    print(f"Profit: {total_amount:.2f} BGN, the gift has been purchased.")
elif total_amount < gift_price:
    print(f"Insufficient money: {(gift_price - total_amount):.2f} BGN.")