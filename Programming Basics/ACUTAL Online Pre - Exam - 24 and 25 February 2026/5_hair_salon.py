day_target = int(input())

money_earned = 0

while True:
    command = input()

    if command == "Closed":
        break

    service_type = command

    if service_type == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            money_earned += 15
        elif haircut_type == "ladies":
            money_earned += 20
        elif haircut_type == "kids":
            money_earned += 10
        else:
            print("Invalid haircut type.")

    elif service_type == "color":
        color_type = input()
        if color_type == "touch up":
            money_earned += 20
        elif color_type == "full color":
            money_earned += 30
        else:
            print("Invalid color type.")
    else:
        break

    if money_earned >= day_target:
        print(f"You have reached your target for the day!")
        break

if money_earned < day_target:
    print(f"Target not reached! You need {(day_target - money_earned)}lv. more.")

print(f"Earned money: {money_earned}lv.")

