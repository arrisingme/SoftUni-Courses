stadium_capacity = int(input())
fans_number = int(input())

count_a = 0
count_b = 0
count_v = 0
count_g = 0

for i in range(fans_number):
    sector = input()
    if sector == "A":
        count_a += 1
    elif sector == "B":
        count_b += 1
    elif sector == "V":
        count_v += 1
    elif sector == "G":
        count_g += 1

print(f"{(count_a / fans_number * 100):.2f}%")
print(f"{(count_b / fans_number * 100):.2f}%")
print(f"{(count_v / fans_number * 100):.2f}%")
print(f"{(count_g / fans_number * 100):.2f}%")
print(f"{(fans_number / stadium_capacity * 100):.2f}%")