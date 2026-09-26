number_of_groups = int(input())
musalla = mont_blanc = Kilimanjaro = k2 = Everest = 0
total_climbers = 0

for _ in range(number_of_groups):
    people_in_group = int(input())
    total_climbers += people_in_group

    if people_in_group <= 5:
        musalla += people_in_group
    elif 6 <= people_in_group <= 12:
        mont_blanc += people_in_group
    elif 13 <= people_in_group <= 25:
        Kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        Everest += people_in_group

print(f"{(musalla / total_climbers * 100):.2f}%")
print(f"{(mont_blanc / total_climbers * 100):.2f}%")
print(f"{(Kilimanjaro / total_climbers * 100):.2f}%")
print(f"{(k2 / total_climbers * 100):.2f}%")
print(f"{(Everest / total_climbers * 100):.2f}%")