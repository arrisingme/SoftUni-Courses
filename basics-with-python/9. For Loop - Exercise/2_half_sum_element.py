from sys import maxsize

max_number = - maxsize
sum_numbers = 0
n = int(input())

for num in range(n):
    new_number = int(input())
    if new_number > max_number:
        max_number = new_number

    sum_numbers += new_number

if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = (max_number - (sum_numbers - max_number))
    print("No")
    print(f"Diff = {abs(diff)}")