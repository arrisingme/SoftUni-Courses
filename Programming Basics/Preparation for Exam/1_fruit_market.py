strawberry_price = float(input())
banana_q = float(input())
orange_q = float(input())
raspberry_q = float(input())
strawberry_q = float(input())

raspberry_price = strawberry_price * 0.50
orange_price = raspberry_price * 0.60
banana_price = raspberry_price * 0.20

total_strawberry_amount = strawberry_price * strawberry_q
total_banana_amount = banana_price * banana_q
total_orange_amount = orange_price * orange_q
total_raspberry_amount = raspberry_price * raspberry_q
total_amount = (total_strawberry_amount + total_banana_amount
                + total_orange_amount + total_raspberry_amount)

print(total_amount)