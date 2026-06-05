mackerel_price_per_kg = float(input())
sprinkle_price_per_kg = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_price_per_kg = (1.60 * mackerel_price_per_kg)
bonito_total_price = (bonito_kg * bonito_price_per_kg)

safrid_price_per_kg = (1.80 * sprinkle_price_per_kg)
safrid_total_price = (safrid_kg * safrid_price_per_kg)

mussels_price_per_kg = 7.50
mussels_total_price = (mussels_kg * mussels_price_per_kg)

total_price_fish = (safrid_total_price +
                    bonito_total_price +
                    mussels_total_price)

total_price_fish = f"{total_price_fish:.2f}"

print(total_price_fish)