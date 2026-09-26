n = int(input())
left = 0
right = 0

for _ in range(n * 2):
    new_number = int(input())

    if _ < n:
        left += new_number
    else:
        right += new_number

if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(left - right)}")