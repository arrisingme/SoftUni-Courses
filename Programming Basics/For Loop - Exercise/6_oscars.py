name = input()
points = float(input())
num_evaluators = int(input())

for i in range(num_evaluators):
    new_evaluators = input()
    point_from_evaluator = float(input())
    points_from_name_lenght = (len(new_evaluators) * point_from_evaluator / 2)

    points += points_from_name_lenght

    if points >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break

else:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")