odd_max = - 100000.00
odd_min = 100000.00
even_max = - 100000.00
even_min = 100000.00
odd_sum = 0
even_sum = 0

n = int(input())

for number in range(1, n + 1):
    next_number = float(input())

    if number % 2 != 0:
        odd_sum += next_number

        if next_number < odd_min:
            odd_min = next_number

        if next_number > odd_max:
            odd_max = next_number

        print(f"OddSum={odd_sum:.2f},")

    else:
        even_sum += next_number

        if next_number < even_min:
            even_min = next_number

        if next_number > even_max:
            even_max = next_number

        print(f"EvenSum={even_sum:.2f},")

    if odd_min == 100000.00:
        print("OddMin=No,")
    else:
        print(f"OddMin={odd_min:.2f},")

    if odd_max == - 100000.00:
        print("OddMax=No,")
    else:
        print(f"OddMax={odd_max:.2f},")

    if even_min == 100000.00:
        print("EvenMin=No,")
    else:
        print(f"EvenMin={even_min:.2f},")

    if even_max == - 100000.00:
        print("EvenMax=No")
    else:
        print(f"EvenMax={even_max:.2f}")


