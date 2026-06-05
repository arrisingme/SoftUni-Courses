n = int(input())

for d1 in range(1, 10):
    for d2 in range(1, 10):
        for d3 in range(1, 10):
            for d4 in range(1, 10):
                sum_1 = d1 + d2
                sum_2 = d3 + d4
                if sum_1 == sum_2:
                    if n % sum_1 == 0:
                        print(f"{d1}{d2}{d3}{d4}", end= " ")