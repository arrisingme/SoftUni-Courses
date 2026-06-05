while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    capacity = int(input())

    if capacity <= 0 :
        print("Capacity must be a positive number")
        continue

    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    tickets_sold = 0

    while tickets_sold < capacity:
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type in ["student", "standard", "kid"]:
            tickets_sold += 1
            if ticket_type == "student":
                student_tickets += 1
            elif ticket_type == "standard":
                standard_tickets += 1
            elif ticket_type == "kid":
                kid_tickets += 1
        else:
            print("Enter a valid ticket type")

    total_tickets = (student_tickets + standard_tickets + kid_tickets)
    total_tickets_pct = total_tickets / capacity * 100

    print(f"{movie_name} - {total_tickets_pct:.2f}% full")

    if total_tickets > 0:
        print(f"Total tickets: {total_tickets}")
        print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
        print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
        print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")


