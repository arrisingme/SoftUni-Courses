minutes = int(input()) * 60
seconds = int(input())
lenght = float(input())
seconds_per_100_m = float(input())

time_to_break = (minutes + seconds)
total_deducted_time = lenght / 120 * 2.5
martins_time = (lenght / 100 * seconds_per_100_m) - total_deducted_time

if martins_time <= time_to_break:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {martins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {(martins_time - time_to_break):.3f} second slower.")