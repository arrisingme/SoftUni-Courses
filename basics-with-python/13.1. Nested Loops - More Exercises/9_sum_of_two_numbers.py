start = int(input())
end = int(input())
magic_number = int(input())

count = 0
found = False

for d1 in range(start, end + 1):
    for d2 in range(start, end + 1):
        count += 1
        if d1 + d2 == magic_number:
            print(f"Combination N:{count} ({d1} + {d2} = {magic_number})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{count} combinations - neither equals {magic_number}")