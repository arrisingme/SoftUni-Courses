name_contestant = input()

starting_points = 301
current_points = 0
shot_counter = 0
successful_shots = 0

while True:
    shot = input()

    if shot == "Retire":
        print(f"{name_contestant} retired after {(shot_counter - successful_shots)} unsuccessful shots.")
        break

    points = int(input())

    if shot == "Single":
        current_points = points
    elif shot == "Double":
        current_points = points * 2
    elif shot == "Triple":
        current_points = points * 3

    shot_counter += 1

    if current_points <= starting_points:
        starting_points -= current_points
        successful_shots += 1

    if starting_points == 0:
        print(f"{name_contestant} won the leg with {successful_shots} shots.")
        break


