voucher_value = int(input())

ticket_count = 0
others_count = 0

while True:
    item = input()

    if item == "End":
        break

    if len(item) > 8:
        price = (ord(item[0]) + ord(item[1]))
    else:
        price = ord(item[0])

    if price <= voucher_value:
        voucher_value -= price
        if len(item) > 8:
            ticket_count += 1
        else:
            others_count += 1

    else:
        break

print(f"{ticket_count}")
print(f"{others_count}")
