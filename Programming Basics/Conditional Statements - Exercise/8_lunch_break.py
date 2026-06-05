series_name = str(input())
series_duration = int(input())
break_duration = int(input())

break_needed_for_lunch = (break_duration * 0.125)
break_to_chill = (break_duration * 0.25)

time_left = int(break_duration - break_needed_for_lunch - break_to_chill)

if time_left >= series_duration:
    print(f"You have enough time to watch {series_name} and left with {time_left - series_duration} minutes free time.")
if time_left < series_duration:
    print(f"You don't have enough time to watch {series_name}, you need {series_duration - time_left} more minutes.")