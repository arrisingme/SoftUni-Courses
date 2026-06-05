name = input()
grade = 1
grade_sum = 0
excluded = 0

while True:
    new_score = float(input())
    if new_score < 4.00:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue

    grade_sum += new_score
    if grade == 12:
        average = grade_sum / 12
        print(f"{name} graduated. Average grade: {average:.2f}")
        break
    grade += 1