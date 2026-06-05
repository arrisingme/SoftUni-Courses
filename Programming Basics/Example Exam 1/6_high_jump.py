target_height = int(input())
starting_bar = target_height - 30

total_jumps = 0
failed_attempts = 0

while True:
    jump = int(input())
    total_jumps += 1

    if jump > starting_bar:
        if starting_bar >= target_height:
            print(f"Tihomir succeeded, he jumped over {target_height}cm after {total_jumps} jumps.")
            break

        starting_bar += 5
        failed_attempts = 0
    else:
        failed_attempts += 1

        if failed_attempts == 3:
            print(f"Tihomir failed at {starting_bar}cm after {total_jumps} jumps.")
            break

