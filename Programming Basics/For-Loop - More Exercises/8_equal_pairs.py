n_pairs = int(input())

current_sum = []

for i in range(n_pairs):
    first_value = int(input())
    second_value = int(input())
    pair_sum = (first_value + second_value)
    current_sum.append(pair_sum)

if all(x == current_sum[0] for x in current_sum):
    print(f"Yes, value={current_sum[0]}")
else:
    max_diff = 0
    for i in range(1, len(current_sum)):
        diff = abs(current_sum[i] - current_sum[i - 1])
        max_diff = max(max_diff, diff)
    print(f"No, maxdiff={max_diff}")
