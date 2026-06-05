students_attended = int(input())
total_grade_gathered = 0

top_students = 0
between_4_5 = 0
between_3_4 = 0
fail = 0

for num in range (students_attended):
    student_grade = float(input())
    if student_grade >= 5.00:
        top_students += 1
        total_grade_gathered += student_grade
    elif 4.00 <= student_grade <= 4.99:
        between_4_5 += 1
        total_grade_gathered += student_grade
    elif 3.00 <= student_grade <= 3.99:
        between_3_4 += 1
        total_grade_gathered += student_grade
    else:
        fail += 1
        total_grade_gathered += student_grade

    avg_success = total_grade_gathered / students_attended

print(f"Top students: {(top_students / students_attended * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_5 / students_attended * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_4 / students_attended * 100):.2f}%")
print(f"Fail: {(fail / students_attended * 100):.2f}%")
print(f"Average: {avg_success:.2f}")