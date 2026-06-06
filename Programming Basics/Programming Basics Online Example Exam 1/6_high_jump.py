height_limit = int(input())

jump_count = 0

for _ in range(height_limit - 30):
    jump_height = int(input())
    if jump_height > height_limit:
        height_limit += 5
        jump_count += 1
        print(f"Tihomir succeeded, he jumped over {jump_height}cm after {jump_count} jumps.")
        break
    else:
        jump_count += 1

    if jump_count == 3:
        print(f"Tihomir failed at {jump_height}cm after {jump_count} jumps.")