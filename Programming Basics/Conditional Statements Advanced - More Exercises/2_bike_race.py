juniors = int(input())
seniors = int(input())
road_type = input()

juniors_tax = 0
seniors_tax = 0
total_contestants = (juniors + seniors)
if road_type == "trail":
    juniors_tax = (juniors * 5.50)
    seniors_tax = (seniors * 7)
elif road_type == "cross-country":
    juniors_tax = (juniors * 8)
    seniors_tax = (seniors * 9.50)
    if total_contestants >= 50:
        juniors_tax -= (juniors_tax * 0.25)
        seniors_tax -= (seniors_tax * 0.25)
elif road_type == "downhill":
    juniors_tax = (juniors * 12.25)
    seniors_tax = (seniors * 13.75)
elif road_type == "road":
    juniors_tax = (juniors * 20)
    seniors_tax = (seniors * 21.50)

total_tax_collected = (juniors_tax + seniors_tax)
total_tax_collected -= (total_tax_collected * 0.05)
print(f"{total_tax_collected:.2f}")