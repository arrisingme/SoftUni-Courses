stage = input()
ticket_type = input()
tickets_quantity = int(input())
picture = input()

price = 0
picture_price = 0

if stage == "Quarter final" and ticket_type == "Standard":
    price = 55.50
elif stage == "Quarter final" and ticket_type == "Premium":
    price = 105.20
elif stage == "Quarter final" and ticket_type == "VIP":
    price = 118.90
elif stage == "Semi final" and ticket_type == "Standard":
    price = 75.88
elif stage == "Semi final" and ticket_type == "Premium":
    price = 125.22
elif stage == "Semi final" and ticket_type == "VIP":
    price = 300.40
elif stage == "Final" and ticket_type == "Standard":
    price = 110.10
elif stage == "Final" and ticket_type == "Premium":
    price = 160.66
elif stage == "Final" and ticket_type == "VIP":
    price = 400

total_price = (price * tickets_quantity)
discount = 0

if 2500 < total_price < 4000:
    discount = total_price * 0.10
elif total_price >= 4000:
    discount = total_price * 0.25

total_price -= discount

if picture == "Y":
    picture_price = (40 * tickets_quantity)

total_price += picture_price

print(f"{total_price:.2f}")
