plastic_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
needed_hours = int(input())

plastic_cost = 1.50
paint_cost = 14.50
thinner_cost = 5
bags = 0.40

total_cost_plastic = (plastic_needed + 2) * plastic_cost
total_cost_paint = (paint_needed + (paint_needed * 0.10 )) * paint_cost
total_cost_thinner = thinner_needed * thinner_cost

total_cost = (total_cost_plastic +
              total_cost_paint +
              total_cost_thinner +
              bags)
labour_cost = (0.30 * total_cost) * needed_hours

final_amount = total_cost + labour_cost

print(final_amount)