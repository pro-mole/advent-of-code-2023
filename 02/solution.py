#!/usr/local/bin/python3
from nis import match
import re

# ==== PART 1 ====
target_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = []

with open("input", "r") as input_file:
    for game_line in input_file.readlines():
        #Parse Game Line
        possible = True
        # Game #: all the round information
        title, round_list = game_line.strip().split(": ")
        game_index = title.split(" ")[-1]
        # round 1; round 2; ...
        rounds = round_list.split("; ")
        for round in rounds:
            draw = {}

            # red X, blue Y ...
            picks = round.split(", ")

            # check validity of pick while parsing it
            for pick in picks:
                quantity, color = pick.split(" ")
                if target_cubes[color] < int(quantity):
                    possible = False
                    print(f"Game {game_index} is impossible! (Round '{round}' due to quantity of {color} cubes)")
                    break
            
            if not possible: break
        if possible: possible_games.append(int(game_index))

print(f"Part 1 Answer: {sum(possible_games)}")

# ==== PART 2 ====
# Power of each game
games = []

with open("input", "r") as input_file:
    for game_line in input_file.readlines():
        minimum_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        #Parse Game Line
        # Game #: all the round information
        title, round_list = game_line.strip().split(": ")
        game_index = title.split(" ")[-1]
        # round 1; round 2; ...
        rounds = round_list.split("; ")
        for round in rounds:
            draw = {}

            # red X, blue Y ...
            picks = round.split(", ")

            # check validity of pick while parsing it
            for pick in picks:
                quantity, color = pick.split(" ")
                minimum_cubes[color] = max(minimum_cubes[color], int(quantity))
        
        game_power = 1
        for color in minimum_cubes:
            game_power *= minimum_cubes[color]
        games.append(game_power)

print(f"Part 2 Answer: {sum(games)}")