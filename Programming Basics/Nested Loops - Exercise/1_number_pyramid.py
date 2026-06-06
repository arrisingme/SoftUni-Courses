n = int(input())

current_number = 1

for rows in range(1, n + 1):
    for column in range(1, rows + 1):
        if current_number > n:
            break
        print(current_number, end=' ')
        current_number += 1

    print()