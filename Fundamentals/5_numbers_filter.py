number_of_lines = int(input())
numbers = []
filtered_numbers = []

for num in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)




# number_of_lines = int(input())
# COMMAND_EVEN = "even"
# COMMAND_ODD = "odd"
# COMMAND_POSITIVE = "positive"
# COMMAND_NEGATIVE = "negative"
#
# numbers = [int(input()) for _ in range(number_of_lines)]
#
# filtered_numbers = []
#
# command = input()
#
# for num in numbers:
#     filtered_command = (
#         (command == COMMAND_EVEN and num % 2 == 0) or
#         (command == COMMAND_ODD and num % 2 != 0) or
#         (command == COMMAND_POSITIVE and num >= 0) or
#         (command == COMMAND_NEGATIVE and num < 0)
#          )
#
#     if filtered_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)