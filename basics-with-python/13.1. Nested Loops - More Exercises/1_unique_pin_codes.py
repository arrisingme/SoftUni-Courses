first_limit = int(input())
second_limit = int(input())
third_limit = int(input())


for digit_1 in range(2, (first_limit + 1), 2):
    for digit_2 in range(2, (second_limit + 1)):
        if digit_2  in [2, 3, 5, 7]:
            for digit_3 in range(2, (third_limit + 1), 2):
                    print(f"{digit_1} {digit_2} {digit_3}")
