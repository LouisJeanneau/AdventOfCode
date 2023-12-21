import re
from copy import deepcopy

import numpy as np

with open("2023_day19_input.txt") as f:
    # with open("2023_day19_sample.txt") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
print("Part 1")
instructionsText = data[0:data.index('')]
instructions = {}
for instruction in instructionsText:
    # print(instruction)
    label = re.findall(r'^[a-z]+', instruction)[0]
    comparaisons = re.findall(r'\{.+\}', instruction)[0][1:-1].split(',')
    comparaisons = [c.split(':') for c in comparaisons]
    # print(label)
    # print(comparaisons)
    instructions[label] = comparaisons

total = 0
for element in data[data.index('') + 1:]:
    # print(element)
    x, m, a, s = [int(i) for i in re.findall(r'\d+', element)]
    # print(x, m, a, s)
    finished = False
    lab = "in"
    while not finished:
        if lab == "A":
            total += x + m + a + s
            finished = True
            break
        if lab == "R":
            finished = True
            break
        for instruction in instructions[lab]:
            if len(instruction) == 1:
                lab = instruction[0]
            elif eval(instruction[0]):
                lab = instruction[1]
                break

print("total = ", total)

# Part 2
print("Part 2")
allCombos = []


def findCondition(target: str, conditionsList):
    print(target)
    for k, v in instructions.items():
        # print("k, v = ", k, v)
        if v[-1] == [target]:
            # Parcours de toute les conditions en ajout inverse
            conditionsListCopy = deepcopy(conditionsList)
            for cond in v[-2::-1]:
                letter = cond[0][0]
                op = cond[0][1]
                value = int(cond[0][2:])
                if op == ">":
                    if value < conditionsListCopy[letter][1]:
                        conditionsListCopy[letter][1] = value + 1
                else:
                    if value > conditionsListCopy[letter][0]:
                        conditionsListCopy[letter][0] = value
            if k == "in":
                allCombos.append(conditionsListCopy)
            else:
                findCondition(k, conditionsListCopy)
            # Parcours entier

        # parcours à partir de la découverte
        for i in range(len(v) - 2, -1, -1):
            if v[i][1] != target:
                continue
            conditionsListCopy = deepcopy(conditionsList)
            cond = v[i][0]
            letter = cond[0]
            op = cond[1]
            value = int(cond[2:])
            if op == "<":
                if value < conditionsListCopy[letter][1]:
                    conditionsListCopy[letter][1] = value
            else:
                if value > conditionsListCopy[letter][0]:
                    conditionsListCopy[letter][0] = value + 1
            for cond in v[0:i]:
                letter = cond[0][0]
                op = cond[0][1]
                value = int(cond[0][2:])
                if op == ">":
                    if value < conditionsListCopy[letter][1]:
                        conditionsListCopy[letter][1] = value + 1
                else:
                    if value > conditionsListCopy[letter][0]:
                        conditionsListCopy[letter][0] = value
            if k == "in":
                allCombos.append(conditionsListCopy)
                continue
            findCondition(k, conditionsListCopy)


# never used (no overlap)
def overlap(group1, group2):
    for i in range(4):
        overlap = max(0, min(group1[i][1], group2[i][1]) - max(group1[i][0], group2[i][0]))
        print(overlap)
    return


t = findCondition("A", {'x': [1, 4001], 'm': [1, 4001], 'a': [1, 4001], 's': [1, 4001]})

intervals = []
for combo in allCombos:
    intervals.append([np.arange(combo[c][0], combo[c][1]) for c in "xmas"])

total = 0
for r in intervals:
    t = 1
    for i in r:
        t *= len(i)
    total += t
print(total)
