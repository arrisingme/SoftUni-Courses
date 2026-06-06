number_attendants = int(input())

back = 0
chest = 0
legs = 0
abss = 0
protein_shake = 0
protein_bar = 0

for _ in range(number_attendants):
    duty = input()
    if duty == "Back":
        back += 1
    elif duty == "Chest":
        chest += 1
    elif duty == "Legs":
        legs += 1
    elif duty == "Abs":
        abss += 1
    elif duty == "Protein shake":
        protein_shake += 1
    elif duty == "Protein bar":
        protein_bar += 1

pct_training = (back + chest + legs + abss) / number_attendants * 100
pct_protein = (protein_shake + protein_bar) / number_attendants * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abss} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{pct_training:.2f}% - work out")
print(f"{pct_protein:.2f}% - protein")
