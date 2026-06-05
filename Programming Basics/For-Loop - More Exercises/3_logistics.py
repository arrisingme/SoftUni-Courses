number_of_loads = int(input())
weights = []
total_price = 0

for number in range(number_of_loads):
    current_weight = int(input())
    weights.append(current_weight)

total_weight = sum(weights)

bus_weight = 0
truck_weight = 0
train_weight = 0

for weight in weights:
    if weight <= 3:
        price = 200
        bus_weight += weight
    elif 4 <= weight <= 11:
        price = 175
        truck_weight += weight
    else:
        price = 120
        train_weight += weight

    total_price += price * weight

    avg_price = total_price / total_weight

percentage_bus = (bus_weight / total_weight) * 100
percentage_truck = (truck_weight / total_weight) * 100
percentage_train = (train_weight / total_weight) * 100

print(f"{avg_price:.2f}")
print(f"{percentage_bus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")