v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

total_ltrs = (p1 + p2) * h
p1_percentage = (p1 * h) / total_ltrs * 100
p2_percentage = (p2 * h) / total_ltrs * 100
percentage = total_ltrs / v * 100

if total_ltrs <= v:
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {(total_ltrs - v):.2f} liters.")