while True:
    student_name = input()

    if student_name == "Voldemort":
        print("You must not speak of that name!")
        break

    name_length = len(student_name)

    if student_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if name_length < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{student_name} goes to Slytherin.")
    elif name_length == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif name_length > 6:
        print(f"{student_name} goes to Hufflepuff.")



