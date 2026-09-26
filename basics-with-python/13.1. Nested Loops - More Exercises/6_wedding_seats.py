last_sector = input()
rows_sector_a = int(input())
odd_seats_number = int(input())

total_seats = 0

sectors_count = ord(last_sector) - ord("A") + 1

for sector in range(sectors_count):
    current_sector = chr(ord("A") + sector)
    current_rows = rows_sector_a + sector
    for row in range(1, current_rows + 1):
        if row % 2 != 0:
            seats_in_row = odd_seats_number
        else:
            seats_in_row = odd_seats_number + 2

        for seat in range(seats_in_row):
            seats_char = chr(ord("a") + seat)
            print(f"{current_sector}{row}{seats_char}")
            total_seats += 1

print(total_seats)