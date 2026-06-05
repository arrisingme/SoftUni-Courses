number_of_easter_breads = int(input())

best_baker = ""
max_points = 0

while True:
    name_baker = input()

    if name_baker == "Stop":
        if best_baker:
            print(f"{best_baker} won competition with {max_points} points!")
            break

    points_baker = int(input())

    if points_baker > max_points:
        best_baker = name_baker
        max_points = points_baker




# print(f"{name_baker} has {max_points} points.")
# print(f"{name_baker} is the new number 1!")




