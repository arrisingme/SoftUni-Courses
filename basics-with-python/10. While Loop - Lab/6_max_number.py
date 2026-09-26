from sys import maxsize
max_number = -maxsize

while True:
    new_number = input()
    if new_number == "Stop":
        break

    number = int(new_number)

    if number > max_number:
        max_number = number

print(max_number)