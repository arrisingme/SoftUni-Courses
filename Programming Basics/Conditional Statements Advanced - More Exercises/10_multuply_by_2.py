while True:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break
    else:
        number *= 2
        print(f"Result: {number:.2f}")