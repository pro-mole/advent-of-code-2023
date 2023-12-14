#!/usr/local/bin/python3

# Card order for Part 1
card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Card order for Part 2
joker_card_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

card_combos = [
    (1,1,1,1,1), # Highest Card
    (2,1,1,1), # Single Pair
    (2,2,1), # Two Pair
    (3,1,1), # Three of a Kind
    (3,2), # Full House
    (4,1), # Four of a Kind
    (5,) # Five of a Kind
]

# Comparator function for Camel Cards hands
# hand: card hand string
# joker: True if J is Joker
def hand_rank(hand, joker=False):
    order = joker_card_order if joker else card_order
    # Unique cards in each hand, ordered according to the card_order
    unique = sorted(list(set(hand)), key = lambda card: order.index(card))

    # Card counts per card, indexed in the same order as the cards in the unique card arrays
    card_count = [hand.count(card) for card in unique]

    # Joker rules: Jokers count for the best possible game; i.e. add number of Jokers to most common card
    if joker and "J" in unique and len(unique) > 1:
        joker_index = unique.index("J")
        joker_count = card_count[joker_index]
        
        unique.pop(joker_index)
        card_count.pop(joker_index)
        max_index = card_count.index(max(card_count))
        card_count[max_index] += joker_count

    # Key for any given hand will be a tuple of combo rank followed by rank of individual cards
    return (card_combos.index(tuple(sorted(card_count, reverse=True))), tuple(order.index(card) for card in hand))

# == PART 1 ==

hands = []

with open("input", "r") as input_file:
    for line in input_file.readlines():
        cards, wager = line.split()
        hands.append((hand_rank(cards, False), cards, wager))

hands.sort()

winnings = 0
for rank, hand in enumerate(hands):
    winnings += (rank+1) * int(hand[2])

print(f"Part 1 Answer: {winnings}")

# == PART 2 ==

hands = []

with open("input", "r") as input_file:
    for line in input_file.readlines():
        cards, wager = line.split()
        hands.append((hand_rank(cards, True), cards, wager))

hands.sort()

winnings = 0
for rank, hand in enumerate(hands):
    winnings += (rank+1) * int(hand[2])

print(f"Part 2 Answer: {winnings}")
