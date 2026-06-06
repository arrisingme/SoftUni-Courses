n_computers = int(input())

total_sales = 0.0
total_rating = 0.0

for _ in range(n_computers):
    realized_sales = 0
    digits = int(input())
    rating = digits % 10
    possible_sales = digits // 10

    if rating < 2 or rating > 6:
        print("Невалиден рейтинг!")
        continue

    if 2 <= rating <= 6:

        if rating == 2:
            realized_sales += possible_sales * 0.0
        elif rating == 3:
            realized_sales += possible_sales * 0.50
        elif rating == 4:
            realized_sales += possible_sales * 0.70
        elif rating == 5:
            realized_sales += possible_sales * 0.85
        elif rating == 6:
            realized_sales += possible_sales * 1.00

        total_sales += realized_sales
        total_rating += rating

if n_computers > 0:
    avg_rating = total_rating / n_computers
else:
    avg_rating = 0.0

print(f"{total_sales:.2f}")
print(f"{avg_rating:.2f}")
