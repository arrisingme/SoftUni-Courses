number_1 = int(input())
number_2 = int(input())


for num in range(number_1, number_2 + 1):
    sum_even = 0
    sum_odd = 0

    for idx, digit in enumerate(str(num)):
        if idx % 2 == 0:
            sum_even += int(digit)
        elif idx % 2 != 0:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(num, end=' ')