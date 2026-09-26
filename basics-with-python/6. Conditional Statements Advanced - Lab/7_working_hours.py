time = int(input())
day_of_the_week = input()
result = ""

if 10 <= time <= 18:
    if ((day_of_the_week == "Monday")
        or (day_of_the_week == "Tuesday")
        or (day_of_the_week == "Wednesday")
        or (day_of_the_week == "Thursday")
        or (day_of_the_week == "Friday")
        or (day_of_the_week == "Saturday")):
        result = "open"
    else:
        result = "closed"
else:
    result = "closed"

print(result)