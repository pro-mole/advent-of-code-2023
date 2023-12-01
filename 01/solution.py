#!/usr/local/bin/python3

# ==== PART 1 ====
numbers = []
with open("input", "r") as input_file:
    for line in input_file.readlines():
        first = None
        last = None
        for char in line:
            if char.isdigit():
                if first == None:
                    first = char
                last = char
        # Save the number for each line
        numbers.append(int(first + last))

print(f"Part 1 Answer: {sum(numbers)}")

# ==== PART 2 ====
import re
numbers = []
digit_library = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digit_pattern = re.compile("[0-9]|" + "|".join(digit_library))

# re.findall does not work due to possible overlapping words (e.g. oneight)
# so instead we will do an exhaustive search on successively smaller substrings
with open("input", "r") as input_file:
    for line in input_file.readlines():
        first = None
        last = None
        
        for start in range(0, len(line)):
            digit_match = digit_pattern.search(line, start)
            if digit_match == None:
                break

            digit = digit_match.group(0) if len(digit_match.group(0)) == 1 else str(digit_library.index(digit_match.group(0)))
            if first == None:
                first = digit
            last = digit    

        numbers.append(int(first + last))

print(f"Part 2 Answer: {sum(numbers)}")