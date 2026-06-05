number_guests = int(input())
money_per_person = float(input())
budget = float(input())

discount = 0
cake = budget * 0.10

if 10 <= number_guests <= 15:
    discount = money_per_person * 0.15
elif 15 < number_guests <= 20:
    discount = money_per_person * 0.20
elif number_guests > 20:
    discount = money_per_person * 0.25

money_per_person -= discount
total_amount = (number_guests * money_per_person) + cake

if budget >= total_amount:
    print(f"It is party time! {(budget - total_amount):.2f} leva left.")
else:
    print(f"No party! {(total_amount - budget):.2f} leva needed.")