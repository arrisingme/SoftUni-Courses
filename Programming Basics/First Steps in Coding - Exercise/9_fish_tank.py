lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
pct = float(input())

volume = lenght_cm * width_cm * height_cm
volume_liters = volume/1000

total_l = volume_liters * (1 - pct/100)

print(total_l)