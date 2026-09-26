men = int(input())
women = int(input())
max_tables = int(input())

occupied_tables = 0

for m in range(1, men + 1):
    for w in range(1, women + 1):
        if occupied_tables >= max_tables:
            break
        print(f"({m} <-> {w})", end= " ")
        occupied_tables += 1
