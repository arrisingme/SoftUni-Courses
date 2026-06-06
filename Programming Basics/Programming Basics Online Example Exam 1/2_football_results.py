first_match_score = input()
second_match_score = input()
third_match_score = input()

won = 0
lost = 0
draw = 0

first_match_score_part = first_match_score.split(":")
team_score = int(first_match_score_part[0])
opponent_score = int(first_match_score_part[1])
if team_score > opponent_score:
    won += 1
elif team_score < opponent_score:
    lost += 1
elif team_score == opponent_score:
    draw += 1

second_match_score_part = second_match_score.split(":")
team_score = int(second_match_score_part[0])
opponent_score = int(second_match_score_part[1])
if team_score > opponent_score:
    won += 1
elif team_score < opponent_score:
    lost += 1
elif team_score == opponent_score:
    draw += 1

third_match_score_part = third_match_score.split(":")
team_score = int(third_match_score_part[0])
opponent_score = int(third_match_score_part[1])
if team_score > opponent_score:
    won += 1
elif team_score < opponent_score:
    lost += 1
elif team_score == opponent_score:
    draw += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")

