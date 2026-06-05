sum_target = int(input())

counter = 0
cash_amount = 0
card_amount = 0
cash_counter = 0
card_counter = 0
total_amount = 0

while True:
    command = input()
    if command == "End":
        break

    payment = int(command)
    counter += 1

    if counter % 2 != 0:
        if payment > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash_amount += payment
            total_amount += payment
            print("Product sold!")

    else:
        if payment < 10:
            print("Error in transaction!")
        else:
            card_counter += 1
            card_amount += payment
            total_amount += payment
            print("Product sold!")

    if total_amount >= sum_target:
        print(f"Average CS: {(cash_amount / cash_counter):.2f}")
        print(f"Average CC: {(card_amount / card_counter):.2f}")
        break

if total_amount < sum_target:
    print("Failed to collect required money for charity.")

