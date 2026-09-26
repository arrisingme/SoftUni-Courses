n = int(input())
l = int(input())

for d1 in range(1, n + 1):
    for d2 in range(1, n + 1):
        for letter1 in range(ord("a"), ord("a") + l):
            for letter2 in range(ord("a"), ord("a") + l):
                for d3 in range(1, n + 1):
                    if d3 > d1 and d3 > d2:
                        print(f"{d1}{d2}{chr(letter1)}{chr(letter2)}{d3}", end=" ")