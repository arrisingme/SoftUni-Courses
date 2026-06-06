country = input()
machine = input()

difficulty = 0
execution = 0
max_score = 20

if country == "Russia" and machine == "ribbon":
    difficulty = 9.100
    execution = 9.400
elif country == "Russia" and machine == "hoop":
    difficulty = 9.300
    execution = 9.800
elif country == "Russia" and machine == "rope":
    difficulty = 9.600
    execution = 9.000
elif country == "Bulgaria" and machine == "ribbon":
    difficulty = 9.600
    execution = 9.400
elif country == "Bulgaria" and machine == "hoop":
    difficulty = 9.550
    execution = 9.750
elif country == "Bulgaria" and machine == "rope":
    difficulty = 9.500
    execution = 9.400
elif country == "Italy" and machine == "ribbon":
    difficulty = 9.200
    execution = 9.500
elif country == "Italy" and machine == "hoop":
    difficulty = 9.450
    execution = 9.350
elif country == "Italy" and machine == "rope":
    difficulty = 9.700
    execution = 9.150

total_score = (difficulty + execution)
not_enough_score_percentage = (max_score - total_score) / max_score * 100

print(f"The team of {country} get {total_score:.3f} on {machine}.")
print(f"{not_enough_score_percentage:.2f}%")