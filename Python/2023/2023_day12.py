import itertools
import re
from collections import defaultdict

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

total = 0
for line in data:
    print(line)
    puzzle, hint = line.split(" ")
    puzzle = '?'.join([puzzle]*5)
    hint = ','.join([hint]*5)
    hint = [int(i) for i in re.findall(r'\d+', hint)]

    l = len(puzzle)
    numberGroup = len(hint)
    states = defaultdict(int)
    states[(0,0)] = 1
    for c in puzzle:
        next = []
        for key, perm_count in states.items():
            group_id, group_amount = key
            if c != '#':
                if group_amount == 0:
                    next.append((group_id, group_amount, perm_count))
                elif group_amount == hint[group_id]:
                    next.append((group_id + 1, 0, perm_count))
            if c != '.':
                if group_id < len(hint) and group_amount < hint[group_id]:
                    next.append((group_id, group_amount + 1, perm_count))
        states.clear()
        for group_id, group_amount, perm_count in next:
            states[(group_id, group_amount)] += perm_count


    def is_valid(group_id, group_amount):
        return group_id == len(hint) or group_id == len(hint) - 1 and group_amount == hint[group_id]


    total += sum(v for k, v in states.items() if is_valid(*k))
    #explore(0, 0, 0)
    #print(total)

print("total = ", total)
