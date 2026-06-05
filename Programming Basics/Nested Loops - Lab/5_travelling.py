while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())
    savings = 0.0

    while savings < budget:
        new_amount = float(input())
        savings += new_amount

    print(f"Going to {destination}!")
