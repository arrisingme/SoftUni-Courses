digit_hundreds = int(input())
digit_tens = int(input())
digit_singles= int(input())

prime_numbers = [2, 3, 5, 7]

for d1 in range(2, digit_hundreds + 1, 2):
    for d2 in prime_numbers:
        if d2 <= digit_tens:
            for d3 in range(2, digit_singles + 1, 2):
                print(f"{d1} {d2} {d3}")