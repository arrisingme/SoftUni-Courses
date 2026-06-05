n = int(input())

for ceiling in range((n + 1) // 2):
    if n % 2:                                       #same as if n % 2 != 0:
        number_of_stars = 1 + ceiling * 2
    else:
        number_of_stars = 2 + ceiling * 2
    spaces = (n - number_of_stars) // 2
    print("-" * spaces + "*" * number_of_stars + "-" * spaces)

for foundation in range(n // 2):
    print("|" + "*" * (n - 2) + "|")


