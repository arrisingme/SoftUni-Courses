p1_name = input()
p2_name = input()

p1_points = 0
p2_points = 0

while True:
    card_input = input()
    if card_input == "End of game":
        break
    card_p1 = int(input())
    card_p2 = int(input())

    if card_p1 > card_p2:
        p1_points += (card_p1 - card_p2)
    elif card_p2 > card_p1:
        p2_points += (card_p2 - card_p1)
    else:
        print("Number wars")
        war_card1 = int(input())
        war_card2 = int(input())
        if war_card1 > war_card2:
            print(f"{p1_name} is winner with {p1_points} points")
        else:
            print(f"{p2_name} is winner with {p2_points} points")

    if p1_points > p2_points:
        print(f"{p1_name} has {p1_points} points")
    else:
        print(f"{p2_name} has {p2_points} points")