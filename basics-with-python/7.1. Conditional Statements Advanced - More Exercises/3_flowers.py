chrysanthemums_quantity = int(input())
roses_quantity = int(input())
tulips_quantity = int(input())
season = input()
holiday_or_not = input()

bucket_arrange = 2.00
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

total_bouquet = ((chrysanthemums_quantity * chrysanthemums_price)
                  + (roses_quantity * roses_price)
                  + (tulips_quantity * tulips_price))

if holiday_or_not == "Y":
    total_bouquet += (total_bouquet * 0.15)
if tulips_quantity > 7 and (season == "Spring" or season == "Summer"):
    total_bouquet -= (total_bouquet * 0.05)
if roses_quantity >= 10 and (season == "Autumn" or season == "Winter"):
    total_bouquet -= (total_bouquet * 0.10)

total_flowers = (chrysanthemums_quantity + roses_quantity + tulips_quantity)

if total_flowers > 20:
    total_bouquet -= (total_bouquet * 0.20)

total_price = (total_bouquet + bucket_arrange)

print(f"{total_price:.2f}")



