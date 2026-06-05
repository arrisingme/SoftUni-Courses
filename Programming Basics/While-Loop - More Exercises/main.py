number_bottles = int(input())
detergent_bottle = 750
total_detergent = number_bottles * detergent_bottle

plates = 0
pots = 0
counter = 0
needed_detergent = 0
is_detergent_enough = True
command = ""

while command != "End":
    command = input()
    if command == "End":
        break

    dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        detergent_needed = dishes * 15
        pots += dishes
    else:
        detergent_needed = dishes * 5
        plates += dishes

    total_detergent -= detergent_needed

    if total_detergent < 0:
        is_detergent_enough = False
        needed_detergent = abs(total_detergent)
        break

if is_detergent_enough:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {needed_detergent} ml. more necessary!")

