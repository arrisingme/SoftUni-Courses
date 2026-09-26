n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        lens = "*" * (2 * n)
    else:
        lens = "*" + "/" * (2 * n - 2) + "*"

    if i == (n - 1) // 2:
        bridge = "|" * n
    else:
        bridge = " " * n

    print(lens + bridge + lens)