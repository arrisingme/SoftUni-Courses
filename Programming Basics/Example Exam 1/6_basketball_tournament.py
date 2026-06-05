tournament_name = input()

total_games = 0
total_wins = 0
total_loses = 0

while tournament_name != "End of tournaments":
    if tournament_name == "End of tournaments":
        break

    matches_count = int(input())

    for game_number in range(1, matches_count + 1):
        total_games += 1
        desi_points = int(input())
        opp_points = int(input())

        difference = abs(desi_points - opp_points)

        if desi_points > opp_points:
            total_wins += 1
            print(f"Game {game_number} of tournament {tournament_name}: win with {difference} points.")
        else:
            total_loses += 1
            print(f"Game {game_number} of tournament {tournament_name}: lost with {difference} points.")

    tournament_name = input()

wins_pct = total_wins / total_games * 100
loses_pct = 100 - wins_pct

print(f"{wins_pct:.2f}% matches win")
print(f"{loses_pct:.2f}% matches lost")
