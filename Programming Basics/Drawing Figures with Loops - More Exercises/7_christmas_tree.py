n = int(input())

print(" " * (n + 1) + "|")

for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (i + 1)
    print(spaces + stars + " | " + stars)

