n = int(input())

char_sum = 0

for i in range(n):
    char = int(input())
    char_sum += char

avg_number = char_sum / n

print(f"{avg_number:.2f}")