w = int(input())
l = int(input())
h = int(input())

total_free_space = w * l * h

while total_free_space >= 0:
    new_input = input()
    if new_input == "Done":
        print(f"{total_free_space} Cubic meters left.")
        break

    total_free_space -= int(new_input)

if total_free_space < 0:
    print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")

