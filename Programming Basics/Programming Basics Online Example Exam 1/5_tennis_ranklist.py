number_tournaments = int(input())
starting_points = int(input())

points_given = 0
wins = 0
total_points = 0

for i in range(number_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        points_given += 2000
        wins += 1
    elif tournament_stage == "F":
        points_given += 1200
    elif tournament_stage == "SF":
        points_given += 720

total_points += points_given
total_points += starting_points

print(f"Final points: {total_points}")
print(f"Average points: {int(points_given / number_tournaments)}")
print(f"{wins / number_tournaments * 100:.2f}%")