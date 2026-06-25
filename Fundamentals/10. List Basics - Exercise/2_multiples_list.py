factor = int(input())
count = int(input())

numbers = []

for multiplier in range(1, count + 1):
    numbers.append(multiplier * factor)

print(numbers)