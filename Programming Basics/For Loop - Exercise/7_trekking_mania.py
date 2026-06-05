number_of_groups = int(input())

musalla = montblanc = kilimanjaro = k2 = everest = 0
total_climbers = 0

for i in range(number_of_groups):
    number_of_people_in_group = int(input())
    total_climbers += number_of_people_in_group
    if number_of_people_in_group <= 5:
        musalla += number_of_people_in_group
    elif 6 >= number_of_people_in_group >= 12:
        montblanc += number_of_people_in_group
    elif 13 >= number_of_people_in_group >= 25:
        kilimanjaro += number_of_people_in_group
    elif 26 >= number_of_people_in_group >= 40:
        k2 += number_of_people_in_group
    elif number_of_people_in_group >= 41:
        everest += number_of_people_in_group

print(f"{(musalla / total_climbers * 100):.2f}%")
print(f"{(montblanc / total_climbers * 100):.2f}%")
print(f"{(kilimanjaro / total_climbers * 100):.2f}%")
print(f"{(k2 / total_climbers * 100):.2f}%")
print(f"{(everest / total_climbers * 100):.2f}%")
