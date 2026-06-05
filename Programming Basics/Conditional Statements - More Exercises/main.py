if 20 <= fuel_quantity <= 25 and fuel_type == "Gasoline":
    price -= 0.08
elif 20 <= fuel_quantity <= 25 and fuel_type == "Diesel":
    price -= 0.08
elif 20 <= fuel_quantity <= 25 and fuel_type == "Gas":
    price -= 0.08
elif fuel_quantity > 25:
    gasoline_price -= 0.10
    diesel_price -= 0.10
    gas_price -= 0.10
    if discount_card == "Yes" and fuel_type == "Gasoline":
        gasoline_price -= 0.18
    elif discount_card == "Yes" and fuel_type == "Diesel":
        diesel_price -= 0.12
    elif discount_card == "Yes" and fuel_type == "Gas":
        gas_price -= 0.08