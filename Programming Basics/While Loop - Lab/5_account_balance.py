deposit = input()
total_in = 0.0

while deposit != "NoMoreMoney":
    amount = float(deposit)
    if amount < 0 :
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total_in += amount
    deposit = input()

print(f"Total: {total_in:.2f}")

