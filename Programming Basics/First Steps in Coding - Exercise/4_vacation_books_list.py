pages_count = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day_to_complete = int(pages_count / pages_per_hour / days)

print(hours_per_day_to_complete)