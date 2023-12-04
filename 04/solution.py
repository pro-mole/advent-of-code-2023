#!/usr/local/bin/python3

# ==== PART 1 ====

total_points = 0

with open("input", "r") as input_file:
    for line in input_file.readlines():
        points = 0
        
        # Parse Input
        # Split game header and relevant input
        _, all_numbers = line.split(": ")

        # Split winning and card numbers
        winning_list, card_list = all_numbers.split("|")

        # Calculate score per card
        winners = set(winning_list.split())
        card = set(card_list.split())
        score = len(winners.intersection(card))
        
        if score > 0:
            points = 2 ** (score - 1)
        
        # Sum them up instead of adding them into an array for a change :P
        total_points += points

print(f"Part 1 Answer: {total_points}")

# ==== PART 2 ====

score_per_card = []

with open("input", "r") as input_file:
    for line in input_file.readlines():
        points = 0
        
        # Parse Input
        # Split game header and relevant input
        _, all_numbers = line.split(": ")

        # Split winning and card numbers
        winning_list, card_list = all_numbers.split("|")

        # Calculate winning numbers per card
        winners = set(winning_list.split())
        card = set(card_list.split())
        score_per_card.append(len(winners.intersection(card)))

card_number = len(score_per_card)

# Part 2: add new cards per winning card
# Start with 1 card of each
scorecards = {i:1 for i in range(card_number)}

for index in range(card_number):
    # For each card below, add as many of them as you won in this card
    for extra in range(score_per_card[index]):
        if index + extra >= card_number-1: break

        scorecards[index + extra + 1] += scorecards[index]

print(f"Part 2 Answer: {sum(scorecards.values())}")