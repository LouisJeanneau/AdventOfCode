import itertools
import re

import constraint as cstt

# with open("2023_day12_input.txt") as f:
with open("2023_day12_sample.txt") as f:
    data = [l.strip() for l in f.readlines()]

# data = open('2023_day12_sample.txt', 'r').read()

print("input = ", data)

# Part 1
# total = 0
# for line in data:
#     # print(line)
#     puzzle, hint = line.split(" ")
#     unknowns = [ind for ind, c in enumerate(puzzle) if c == "?"]
#     dots = [ind for ind, c in enumerate(puzzle) if c == "."]
#     hashtags = [ind for ind, c in enumerate(puzzle) if c == "#"]
#     hint = [int(i) for i in re.findall(r'\d+', hint)]
#     sumHint = sum(hint)
#     sumHash = len(hashtags)
#     for combi in list(itertools.product([0, 1], repeat=len(unknowns))):
#         if sum(combi) + sumHash != sumHint:
#             continue
#         copyLine = list(line)
#         for index, value in enumerate(unknowns):
#             copyLine[value] = '#' if combi[index]==1 else '.'
#         groups = re.findall(r'#+', ''.join(copyLine))
#         if [len(g) for g in groups] == hint:
#             total += 1
# print("total = ", total)


# Part 2
for line in data:
    print(line)
    puzzle, hint = line.split(" ")
    # puzzle = '?'.join([puzzle]*5)
    # hint = ','.join([hint]*5)
    hint = [int(i) for i in re.findall(r'\d+', hint)]
    permutations = dict()
    l = len(puzzle)
    numberGroup = len(hint)
    total = 0
    states = dict()
    states[(0,0)] = 1
    for c in puzzle:
        nextSteps = []



    def explore(index, group, amount):
        global total
        if line[index] == " ":
            if group == numberGroup and amount == 0:
                total += 1
            elif group == numberGroup - 1 and amount == hint[group]:
                total += 1
        elif group < numberGroup and hint[group] < amount:
            return
        elif group >= numberGroup:
            return

        elif line[index] == "?":
            # behave as #
            explore(index + 1, group, amount + 1)
            # behave as .
            explore(index + 1, group + int(amount != 0), 0)
        elif line[index] == "#":
            explore(index + 1, group, amount + 1)
        elif line[index] == ".":
            if amount == 0:
                explore(index + 1, group, 0)
            elif amount == hint[group]:
                explore(index + 1, group + int(amount != 0), 0)


    explore(0, 0, 0)
    print(total)

print("total = ", total)
