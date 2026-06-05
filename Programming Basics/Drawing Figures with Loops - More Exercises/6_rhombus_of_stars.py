n = int(input())

for rows_up in range(1, n + 1):
    print(" " * (n - rows_up) + "* " + "* " * (rows_up - 1))
for rows_down in range(n - 1, 0, -1):
    print(" " * (n - rows_down) + "* " + "* " * (rows_down - 1))