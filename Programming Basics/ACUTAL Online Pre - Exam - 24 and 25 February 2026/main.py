day_target = int(input())

money_earned = 0

while True:
    command = input()
    if command == "Closed":
        break

    price = 0

    if command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            price = 15
        elif haircut_type == "ladies":
            price = 20
        elif haircut_type == "kids":
            price = 10

    elif command == "color":
        color_type = input()
        if color_type == "touch up":
            price = 20
        elif color_type == "full color":
            price = 30

    money_earned += price

    if money_earned >= day_target:
        print(f"You have reached your target for the day!")
        break

print(f"Earned money: {money_earned}lv.")
if money_earned >= day_target:
    print(f"Target not reached! You need {(day_target - money_earned)}lv. more.")




