#!/usr/local/bin/python3

# ==== PART 1 ====

# Sparse matrix to store numbers and symbols that will mark our selected numbers
number_matrix = [] # (number, coordinates of the first number [line, char] )
marker_matrix = [] # (marker, coordinates of the marker [line, char] )

part_numbers = set()

with open("input", "r") as input_file:
    line_number = 0
    num_buffer = ""
    for line in input_file.readlines():
        for index in range(len(line)):
            if line[index].isdigit():
                num_buffer += line[index]
            else:
                if num_buffer != "":
                    number_matrix.append((num_buffer, (line_number, index - len(num_buffer))))
                    num_buffer = ""
                if line[index] != '.' and not line[index].isspace():
                    marker_matrix.append((line[index], (line_number, index)))
        line_number += 1
    
for marker, (y, x) in marker_matrix:
    for num, (num_y, num_x) in number_matrix:
        if (num, num_y, num_x) in part_numbers: continue # no repeats

        dy = abs(num_y - y)
        if dy > 1: continue
        
        dx = 0 # assume number is directly above/below the mark
        if num_x > x: # number is to the right of the mark
            dx = abs(x - num_x)
        elif num_x + len(num)-1 < x: # number is to the left of the mark
            dx = abs(num_x + len(num)-1 - x)
        if dy <= 1 and dx <= 1: # check adjacent part
            part_numbers.add((num, num_y, num_x))

print(f"Part 1 Answer: {sum([int(part[0]) for part in part_numbers])}")

# ==== PART 2 ====

gears = []

for marker, (y, x) in marker_matrix:
    if marker == '*':
        parts_linked = []
        for num, (num_y, num_x) in number_matrix:
            dy = abs(num_y - y)
            if dy > 1: continue
            
            dx = 0 # assume number is directly above/below the mark
            if num_x > x: # number is to the right of the mark
                dx = abs(x - num_x)
            elif num_x + len(num)-1 < x: # number is to the left of the mark
                dx = abs(num_x + len(num)-1 - x)
            if dy <= 1 and dx <= 1: # check adjacet part
                parts_linked.append(int(num))
        
        if len(parts_linked) == 2:
            gears.append(parts_linked[0] * parts_linked[1])

print(f"Part 2 Answer: {sum(gears)}")