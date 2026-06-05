m = int(input())

found_combos = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    control_value = (a * b) + (c * d)
                    if control_value == m:
                        found_combos.append(f"{a}{b}{c}{d} ")
if found_combos:
    print("".join(found_combos))
    if len(found_combos) >= 4:
        print(f"Password: {found_combos[3]}")
    else:
        print("No!")
else:
    print("No!")
