turns = int(input())
point_per_turn = 0
counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 =0
counter_40_50 = 0
counter_invalid = 0

for i in range(turns):
    new_turn = int(input())
    if new_turn < 0 or new_turn > 50:
        point_per_turn /= 2
        counter_invalid += 1
        continue

    if new_turn >= 0:
        if 0 <= new_turn <= 9:
            point_per_turn += 0.20 * new_turn
            counter_0_9 += 1
        elif 10 <= new_turn <= 19:
            point_per_turn += 0.30 * new_turn
            counter_10_19 += 1
        elif 20 <= new_turn <= 29:
            point_per_turn += 0.40 * new_turn
            counter_20_29 += 1
        elif 30 <= new_turn <= 39:
            point_per_turn += 50
            counter_30_39 += 1
        elif 40 <= new_turn <= 50:
            point_per_turn += 100
            counter_40_50 += 1

print(f"{point_per_turn:.2f}")
print(f"From 0 to 9: {(counter_0_9 / turns * 100):.2f}%")
print(f"From 10 to 19: {(counter_10_19 / turns * 100):.2f}%")
print(f"From 20 to 29: {(counter_20_29 / turns * 100):.2f}%")
print(f"From 30 to 39: {(counter_30_39 / turns * 100):.2f}%")
print(f"From 40 to 50: {(counter_40_50 / turns * 100):.2f}%")
print(f"Invalid numbers: {(counter_invalid / turns * 100):.2f}%")





