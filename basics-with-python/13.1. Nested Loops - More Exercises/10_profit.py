number_coins_1 = int(input())
number_coins_2 = int(input())
number_banknotes_5 = int(input())
total_sum = int(input())


for coin_1 in range(number_coins_1 + 1):
    for coin_2 in range(number_coins_2 + 1):
        for banknotes in range(number_banknotes_5 + 1):
            total_value = ((coin_1 * 1) + (coin_2 * 2) + (banknotes * 5))
            if total_value == total_sum:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. + {banknotes} * 5 lv. = {total_sum} lv.")