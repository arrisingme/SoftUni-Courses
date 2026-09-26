shape = input()

from math import pi

if shape == "square":
    square_side = float(input())
    shape_area = square_side * square_side

elif shape == "rectangle":
    rectangle_a = float(input())
    rectangle_b = float(input())
    shape_area = rectangle_a * rectangle_b

elif shape == "circle":
    circle_r = float(input())
    shape_area = pi * (circle_r ** 2)

elif shape == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    shape_area = (triangle_side * triangle_height) / 2

print(f"{shape_area:.3f}")