total_pained_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for _ in range(total_pained_eggs):
    colour = input()

    if colour == "red":
        red += 1
    elif colour == "orange":
        orange += 1
    elif colour == "blue":
        blue += 1
    elif colour == "green":
        green += 1

max_eggs = red
max_colour = "red"

if orange > max_eggs:
    max_eggs = orange
    max_colour = "orange"

elif blue > max_eggs:
    max_eggs = blue
    max_colour = "blue"

elif green > max_eggs:
    max_eggs = green
    max_colour = "green"

elif red > max_eggs:
    max_eggs = red
    max_colour = "red"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_colour}")
