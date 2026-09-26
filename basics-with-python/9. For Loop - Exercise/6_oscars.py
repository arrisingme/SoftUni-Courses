name = input()
points = float(input())
number_of_evaluators = int(input())

for _ in range(number_of_evaluators):
    new_evaluators = input()
    points_given = float(input())
    points_for_actor = ((len(new_evaluators) * points_given) / 2)

    points += points_for_actor

    if points_given >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f} points!")
        break
else:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")
