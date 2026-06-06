pack_pens_price = 5.80
pack_marker_price = 7.20
detergent_price =  1.20

pens_q = int(input())
markers_q = int(input())
detergent_liters = int(input())
discount = float(input())/100

discount_only = (pens_q * pack_pens_price + markers_q * pack_marker_price + detergent_liters * detergent_price) * discount
bill = (pens_q * pack_pens_price + markers_q * pack_marker_price + detergent_liters * detergent_price) - discount_only

print(bill)