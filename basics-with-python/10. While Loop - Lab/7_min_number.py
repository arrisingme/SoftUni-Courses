min_number = 1000000

number = input()

while number != "Stop":
    new_number = int(number)

    if new_number < min_number:
        min_number = new_number
    number = input()

print(min_number)