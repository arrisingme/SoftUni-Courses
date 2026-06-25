deck_of_cards = input().split()
number_of_shuffles = int(input())

for current_shuffle in range(number_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_side = deck_of_cards[:middle_of_deck]
    right_side = deck_of_cards[middle_of_deck:]
    deck_after_shuffling = []
    for index in range(len(left_side)):
        deck_after_shuffling.append(left_side[index])
        deck_after_shuffling.append(right_side[index])
    deck_of_cards = deck_after_shuffling.copy()

print(deck_of_cards)
