#!/usr/local/bin/python3

# == PART 1 ==

galaxies = []

min_range = []
max_range = []
with open('input', 'r') as input_file:
    row = 0
    line = input_file.readline().strip()
    while line:
        col = 0
        for point in line:
            if point == '#':
                if len(min_range) == 0:
                    min_range = [row, col]
                    max_range = [row, col]
                else:
                    min_range = [min(min_range[0], row), min(min_range[1], col)]
                    max_range = [max(max_range[0], row), max(max_range[1], col)]
                galaxies.append((row, col))
            col += 1
        row += 1
        line = input_file.readline().strip()

# Find empty rows and columns
empty_rows = set(range(min_range[0], max_range[0]))
empty_cols = set(range(min_range[1], max_range[1]))
for x, y in galaxies:
    if x in empty_rows: empty_rows.remove(x)
    if y in empty_cols: empty_cols.remove(y)

# Calculate path between galaxies and then add extra columns and rows between them
total_path = 0
for origin in range(len(galaxies)):
    for destination in range(origin+1, len(galaxies)):
        g_from = galaxies[origin]
        g_to = galaxies[destination]
        path_length = abs(g_from[0] - g_to[0]) + abs(g_from[1] - g_to[1])
        for row in range(min(g_from[0], g_to[0]), max(g_from[0], g_to[0])):
            if row in empty_rows: path_length += 1
        for col in range(min(g_from[1], g_to[1]), max(g_from[1], g_to[1])):
            if col in empty_cols: path_length += 1
        total_path += path_length

print(f"Part 1 Answer: {total_path}")

# == PATH 2 ==

# Calculate path between galaxies and then add extra columns and rows between them
# except now we add 999999 extra spaces instead of 1
total_path = 0
for origin in range(len(galaxies)):
    for destination in range(origin+1, len(galaxies)):
        g_from = galaxies[origin]
        g_to = galaxies[destination]
        path_length = abs(g_from[0] - g_to[0]) + abs(g_from[1] - g_to[1])
        for row in range(min(g_from[0], g_to[0]), max(g_from[0], g_to[0])):
            if row in empty_rows: path_length += 999999
        for col in range(min(g_from[1], g_to[1]), max(g_from[1], g_to[1])):
            if col in empty_cols: path_length += 999999
        total_path += path_length

print(f"Part 2 Answer: {total_path}")