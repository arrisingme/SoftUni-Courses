holidays_per_year = int(input())

total_days_year = 365
toms_norm = 30000
total_play_time_week = (total_days_year - holidays_per_year) * 63
total_play_time_holiday = (holidays_per_year * 127)
total_play_time = (total_play_time_holiday + total_play_time_week)
difference_norm_minutes = abs(toms_norm - total_play_time)

total_hours =  difference_norm_minutes // 60
total_minutes = difference_norm_minutes % 60

if total_play_time > toms_norm:
    print("Tom will run away")
    print(f"{total_hours} hours and {total_minutes} minutes more for play")
elif total_play_time < toms_norm:
    print("Tom sleeps well")
    print(f"{total_hours} hours and {total_minutes} minutes less for play")