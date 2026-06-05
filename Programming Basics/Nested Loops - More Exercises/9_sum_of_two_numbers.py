start = int(input())
end = int(input())
magic_number = int(input())

count = 0
found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1
        if i + j == magic_number:
            print(f"Combination N:{count} ({i} + {j} = {magic_number})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{count} combinations - neither equals {magic_number}")