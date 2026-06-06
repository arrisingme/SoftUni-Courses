budget = float(input())
total_video_cards = int(input())
total_cpu = int(input())
total_rams = int(input())

video_card_price = 250
cpu_price = (total_video_cards * video_card_price) * 0.35
ram_price = (total_video_cards * video_card_price) * 0.10

total_amount = (total_video_cards * video_card_price) + \
               (total_cpu * cpu_price) + \
               (total_rams * ram_price)

if total_video_cards > total_cpu:
    discount = (total_amount * 0.15)
    total_amount -= discount

difference = abs(budget - total_amount)

if  budget >= total_amount:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

