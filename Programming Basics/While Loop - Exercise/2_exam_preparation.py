max_fails = int(input())
max_fails_counter = max_fails
total_tasks = 0
total_tasks_score = 0
last_problem = ""

while max_fails_counter > 0:
    new_task = input()

    if new_task == "Enough":
        print(f"Average score: {total_tasks_score / total_tasks:.2f}")
        print(f"Number of problems: {total_tasks}")
        print(f"Last problem: {last_problem}")
        break

    last_problem = new_task
    total_tasks += 1

    task_score = int(input())
    total_tasks_score += task_score

    if task_score <= 4:
        max_fails_counter -= 1
        if max_fails_counter <= 0:
            print(f"You need a break, {max_fails} poor grades.")
            break