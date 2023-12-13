import itertools
import re

import constraint as cstt

# with open("2023_day12_input.txt") as f:
with open("2023_day12_sample.txt") as f:
   data = [l.strip() for l in f.readlines()]

# data = open('2023_day12_sample.txt', 'r').read()

print("input = ", data)

# Part 1
total = 0
for line in data:
    # print(line)
    puzzle, hint = line.split(" ")
    unknowns = [ind for ind, c in enumerate(puzzle) if c == "?"]
    dots = [ind for ind, c in enumerate(puzzle) if c == "."]
    hashtags = [ind for ind, c in enumerate(puzzle) if c == "#"]
    hint = [int(i) for i in re.findall(r'\d+', hint)]
    sumHint = sum(hint)
    sumHash = len(hashtags)
    for combi in list(itertools.product([0, 1], repeat=len(unknowns))):
        if sum(combi) + sumHash != sumHint:
            continue
        copyLine = list(line)
        for index, value in enumerate(unknowns):
            copyLine[value] = '#' if combi[index]==1 else '.'
        groups = re.findall(r'#+', ''.join(copyLine))
        if [len(g) for g in groups] == hint:
            total += 1
print("total = ", total)

# Part 2
