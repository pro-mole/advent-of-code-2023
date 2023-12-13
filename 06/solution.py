#!/usr/local/bin/python3

# ==== PART 1 ====

times = []
distances = []

with open("input", "r") as input_file:
    # Basic parse
    times = input_file.readline().split()[1:]
    distances = input_file.readline().split()[1:]

# The Winning Range for each race is the minimum and maximum time you can press the button to win
winning_range = []

for race_index in range(len(times)):
    race_time = int(times[race_index])
    race_distance = int(distances[race_index])
    print(f"{race_time}ms {race_distance}mm")
    min_time = 1
    max_time = race_time

    while (race_time - min_time) <= (race_distance / min_time):
        min_time += 1
    print(f"Minimum charge time: {min_time} (race won in {race_distance / min_time}ms )")

    while (race_time - max_time) <= (race_distance / max_time):
        max_time -= 1
    print(f"Maximum charge time: {max_time} (race won in {race_distance / max_time}ms )")

    winning_range.append((min_time, max_time))

print(winning_range)
answer = 1
for lower, higher in winning_range:
    answer *= higher - lower + 1
print(f"Part 1 Answer: {answer}")

# ==== PART 2 ====

time = ""
distance = ""

with open("input", "r") as input_file:
    # Basic parse
    for record in input_file.readline().split()[1:]:
        time = time + record
    for record in input_file.readline().split()[1:]:
        distance = distance + record

race_time = int(time)
race_distance = int(distance)

min_time = 1
max_time = race_time

# Code works but could be more efficient; perhaps a binary search?
while (race_time - min_time) <= (race_distance / min_time):
    min_time += 1
print(f"Minimum charge time: {min_time} (race won in {race_distance / min_time}ms )")

while (race_time - max_time) <= (race_distance / max_time):
    max_time -= 1
print(f"Maximum charge time: {max_time} (race won in {race_distance / max_time}ms )")

print(f"Part 2 Answer: {max_time - min_time + 1}")