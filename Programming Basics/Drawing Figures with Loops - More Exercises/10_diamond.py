n = int(input())

# Първоначален брой тирета отляво и отдясно
left_right = (n - 1) // 2

# Цикъл за горната част (включително средния ред)
# Броят на редовете в горната част е (n + 1) // 2
for i in range((n + 1) // 2):
    # Изчисляваме средните тирета
    mid = n - 2 * left_right - 2

    print("-" * left_right, end="")
    print("*", end="")

    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")

    print("-" * left_right)

    left_right -= 1

# Цикъл за долната част
left_right = 1

for i in range((n - 1) // 2):
    mid = n - 2 * left_right - 2

    # Тъй като при n=1 или n=2 долната част не трябва да се изпълнява,
    # този цикъл автоматично ще бъде пропуснат при тях.
    if mid < -1:
        break

    print("-" * left_right, end="")
    print("*", end="")

    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")

    print("-" * left_right)

    left_right += 1