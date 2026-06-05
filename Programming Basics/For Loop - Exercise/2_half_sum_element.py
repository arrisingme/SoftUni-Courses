import sys

n = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for i in range(0, n):
    number = int(input())

    if number > max_number:
        max_number = number
    sum_numbers += number

if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_numbers = sum_numbers - max_number
    print("No")
    print(f"Diff = {abs(max_number - sum_numbers)}")