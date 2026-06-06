start_range = input() #2345
end_range = input() #6789

start1, start2, start3, start4 = map(int, start_range)
end1, end2, end3, end4 = map(int, end_range)

for digit_1 in range(start1, end1 + 1):
    if digit_1 % 2 == 0:
        continue
    for digit_2 in range(start2, end2 + 1):
        if digit_2 % 2 == 0:
            continue
        for digit_3 in range(start3, end3 + 1):
            if digit_3 % 2 == 0:
                continue
            for digit_4 in range(start4, end4 + 1):
                if digit_4 % 2 == 0:
                    continue
                print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=' ')
