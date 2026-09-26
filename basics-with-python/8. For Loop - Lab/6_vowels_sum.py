text = input()
points_vowels = 0

for char in text:
    if char == "a":
        points_vowels += 1
    elif char == "e":
        points_vowels += 2
    elif char == "i":
        points_vowels += 3
    elif char == "o":
        points_vowels += 4
    elif char == "u":
        points_vowels += 5

print(points_vowels)