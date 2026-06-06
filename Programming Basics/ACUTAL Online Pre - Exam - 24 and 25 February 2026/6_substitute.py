k = int(input())
l = int(input())
m = int(input())
n = int(input())

valid_changes = 0

for digit_1 in range(k, 9):
    for digit_2 in range(9, l - 1, -1):
        for digit_3 in range(m, 9):
            for digit_4 in range(9, n - 1, -1):
                if digit_1 % 2 == 0 and digit_3 % 2 == 0 and digit_2 % 2 != 0 and digit_4 % 2 != 0:

                    player_1 = str(digit_1) + str(digit_2)
                    player_2 = str(digit_3) + str(digit_4)

                    if player_1 == player_2:
                        print("Cannot change the same player.")
                    else:
                        print(f"{player_1} - {player_2}")

                        valid_changes += 1

                    if valid_changes == 6:
                        exit(0)

