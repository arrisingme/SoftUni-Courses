start = int(input())
end = int(input())
d1 = 0
d2 = 0
d3 = 0
d4 = 0

d2_d3_sum = d2 + d3

for d1 in range(start, end + 1):
    for d2 in range(start, end + 1):
        for d3 in range(start, end + 1):
            for d4 in range(start, end + 1):
                if (d1 % 2 == 0 and d4 % 2 != 0) or (d4 % 2 == 0 and d1 % 2 != 0):
                   if d1 > d4:
                       if (d2 + d3) % 2 == 0:
                        print(f"{d1}{d2}{d3}{d4}", end=" ")
