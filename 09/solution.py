#!/usr/local/bin/python3

# Extrapolate a sequence of numbers based on successive sequences of differences (i.e. derivation)
def extrapolate(seq, reverse=False):
    diff_seq = [seq]
    level = 0

    # Continue until the difference is all 0s
    while set(diff_seq[level]) != set([0]):
        cur_diff = diff_seq[level]
        new_diff = []
        for idx in range(len(cur_diff)-1):
            new_diff.append(cur_diff[idx+1]-cur_diff[idx])
        diff_seq.append(new_diff)
        level += 1

    extrapolated = 0
    while level >= 0:
        if reverse:
            extrapolated = diff_seq[level][0] - extrapolated # == PART 2 ==
        else:
            extrapolated += diff_seq[level][-1] # == PART 1 ==
        level -= 1
    
    return extrapolated

total = 0

with open("input", "r") as input_file:
    for line in input_file.readlines():
        total += extrapolate([int(val) for val in line.split()])

print(f"Part 1 Answer: {total}")

total = 0

with open("input", "r") as input_file:
    for line in input_file.readlines():
        total += extrapolate([int(val) for val in line.split()], True)

print(f"Part 2 Answer: {total}")
