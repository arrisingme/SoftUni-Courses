name_p1 = input()
name_p2 = input()

points_p1 = 0
points_p2 = 0

command = input()

while command != "End of game":
    card_p1 = int(command)
    card_p2 = int(input())

    if card_p1 > card_p2:
        points_p1 += (card_p1 - card_p2)
    elif card_p2 > card_p1:
        points_p2 += (card_p2 - card_p1)
    else:
        print("Number wars!")

        war_card_p1 = int(input())
        war_card_p2 = int(input())

        if war_card_p1 > war_card_p2:
            print(f"{name_p1} is winner with {points_p1} points")
        else:
            print(f"{name_p2} is winner with {points_p2} points")

        break

    command = input()

else:
    print(f"{name_p1} has {points_p1} points")
    print(f"{name_p2} has {points_p2} points")


