starting_q = int(input())

current_q = starting_q
eggs_sold = 0

command = input()

while command != "Close":
    quantity = int(input())
    if command == "Buy":
        quantity = int(quantity)
        if current_q < quantity:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {current_q}.")
            break
        else:
            current_q -= quantity
            eggs_sold += quantity

    elif command == "Fill":
        current_q += quantity
    else:
        print("Invalid command!")

    command = input()

if command == "Close":
    print(f"Store is closed!")
    print(f"{eggs_sold} eggs sold.")