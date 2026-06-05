period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for number in range(period):
    patients = int(input())
    if  patients <= doctors:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors

    if ((number + 1) % 3 == 2) and (untreated_patients > 0):
        doctors += 1

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")


