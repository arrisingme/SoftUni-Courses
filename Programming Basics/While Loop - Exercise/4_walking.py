goal = 10000
steps_counter = 0

while True:
    new_input = input()
    if new_input == "Going home":
        steps_to_home = int(input())
        steps_counter += steps_to_home
        if steps_counter < goal:
            print(f"{goal - steps_counter} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{steps_counter - goal} steps over the goal!")
        break

    steps_counter += int(new_input)

    if steps_counter >= goal:
        print("Goal reached! Good job!")
        print(f"{steps_counter - goal} steps over the goal!")
        break

