from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
point_given = 0
total_points = 0
wins = 0

for i in range(number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        point_given += 2000
        wins += 1
    elif tournament_stage == "F":
        point_given += 1200
    elif tournament_stage == "SF":
        point_given += 720
total_points = (point_given - starting_points)
point_given += starting_points

print(f"Final points: {point_given}")
print(f"Average points: {floor((point_given - starting_points)/ number_of_tournaments)}")
print(f"{wins / number_of_tournaments * 100:.2f}%")