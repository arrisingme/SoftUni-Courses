l_mtrs = float(input())
w_mtrs = float(input())

l_cm = (l_mtrs * 100)
w_cm = (w_mtrs * 100)

available_w = (w_cm - 100)
available_rows = (l_cm // 120)
available_desks = (available_w // 70)

total_desks = (available_rows * available_desks) - 3

print(total_desks)