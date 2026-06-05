start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination = 0
found = False

for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        combination += 1
        if (i + j == magic_number):
            found = True
            print(f"Combination N:{combination} ({i} + {j} = {magic_number})")
            break
    if found:
        break

if not found:
    print(f"{combination} combinations - neither equals {magic_number}")