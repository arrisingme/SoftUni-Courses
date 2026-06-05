x = float(input())
y = float(input())
h = float(input())

area_front = (x * x - (1.2 * 2))
area_back = (x * x)
area_double_sides = ((x * y) - (1.5 * 1.5)) * 2

total_area_green_paint_needed = (area_front + area_back + area_double_sides) / 3.4

area_roof_rectangles = (y * x) * 2
area_roof_triangles = ((x * h) / 2) * 2

total_area_red_paint_needed = (area_roof_rectangles + area_roof_triangles) / 4.3

total_area_green_paint_needed = f"{total_area_green_paint_needed:.2f}"
total_area_red_paint_needed = f"{total_area_red_paint_needed:.2f}"

print(total_area_green_paint_needed)
print(total_area_red_paint_needed)