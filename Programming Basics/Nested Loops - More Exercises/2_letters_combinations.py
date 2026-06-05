char_start = input()
char_end = input()
char_skip = input()

start = ord(char_start)
end = ord(char_end)
skip = ord(char_skip)

count = 0

for first in range(start, end + 1):
    if first == skip:
        continue
    for second in range(start, end + 1):
        if second == skip:
            continue
        for third in range(start, end + 1):
             if third == skip:
                continue

            count += 1
            combo = f"{chr(first)}{chr(second)}{chr(third)}"
            print(combo, end= " ")

print(count)