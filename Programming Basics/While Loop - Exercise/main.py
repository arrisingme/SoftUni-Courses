current_title = input()

while current_title != "No More Books":
    new_title = input()

    if new_title == current_title:
        print(f"You checked {counter} books and found it.")
        break

    if new_title == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break

    counter += 1