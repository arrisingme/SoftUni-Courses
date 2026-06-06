sq_m_q = float(input())
price_sq_m = 7.61
total_amount = sq_m_q * price_sq_m
total_discount = 0.18 * total_amount
final_price = total_amount - total_discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {total_discount} lv.")