#!/usr/local/bin/python3

# ==== PART 1 ====

# Convert a source list into a destination list using a list of rules
# List of rules is a list of tuples containing (destination-range, source-range, length)
def convert(source, rules):
    destination = []
    for src in source:
        src_value = int(src)
        converted = False
        for dst_first, src_first, rule_range in rules:
            if src_value >= src_first and src_value < src_first+rule_range:
                destination.append(dst_first + (src_value - src_first))
                converted = True
                break
        
        if not converted:
            destination.append(src_value)
    
    return destination

with open("input", "r") as input_file:
    # First line is the seed list
    seed_line = input_file.readline()
    work_list = seed_line.split()[1:] # discard the title element "seeds:"

    # Process the subsequent chain of conversions without really caring what they are for
    # They come in sequence and describe the rules in the same way, so we can just
    # convert seeds into the next input and so on
    next_line = input_file.readline()
    while next_line:
        conversion_rules = []
        # Discard header line
        print(f" ==> {input_file.readline()}")

        next_line = input_file.readline()
        while next_line.strip():
            dest_range, src_range, length = next_line.split()
            conversion_rules.append((int(dest_range), int(src_range), int(length)))
            next_line = input_file.readline()
        
        work_list = convert(work_list, conversion_rules)

print(f"Part 1 Answer: {min(work_list)}")

# ==== PART 2 - IN PROGRESS ====

# Almost the same, but the seed list will be a little more expanded :}

with open("input", "r") as input_file:
    # First line is the seed list
    seed_line = input_file.readline()
    
    seed_list = seed_line.split()[1:] # discard the title element "seeds:"
    work_list = set()
    for i in range(len(seed_list) // 2): # expand the seed list correctly
        start = int(seed_list[i*2])
        end = start + int(seed_list[i*2 + 1])
        for seed in range(start, end):
            work_list.add(seed)

    # Process the subsequent chain of conversions without really caring what they are for
    # They come in sequence and describe the rules in the same way, so we can just
    # convert seeds into the next input and so on
    next_line = input_file.readline()
    while next_line:
        conversion_rules = []
        # Discard header line
        print(f" ==> {input_file.readline()}")

        next_line = input_file.readline()
        while next_line.strip():
            dest_range, src_range, length = next_line.split()
            conversion_rules.append((int(dest_range), int(src_range), int(length)))
            next_line = input_file.readline()
        
        work_list = convert(work_list, conversion_rules)

print(f"Part 2 Answer: {min(work_list)}")