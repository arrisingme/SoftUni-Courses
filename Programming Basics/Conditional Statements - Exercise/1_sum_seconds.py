time_first = int(input())
time_second = int(input())
time_third = int(input())

total_seconds = time_first + time_second + time_third

minutes = total_seconds // 60
seconds_left = total_seconds % 60

if seconds_left <10:
    print(f"{minutes}:0{seconds_left}")
else:
    print(f"{minutes}:{seconds_left}")