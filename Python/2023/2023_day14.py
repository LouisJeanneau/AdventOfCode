import itertools
import re
import numpy as np

with open("2023_day14_input.txt") as f:
# with open("2023_day14_sample.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# data = open('2023_day14_sample.txt', 'r').read()

print("input = ", data)

# Part 1
print("Part 1")
map = np.array(data)
map = map.T
cubes = np.where(map == '#')
cubesPositions = list(zip(cubes[0], cubes[1]))
cubesPositions.extend([(i, -1) for i in range(len(map))])
cubesPositions.extend([(i, len(map[0])) for i in range(len(map))])
cubesPositions = sorted(cubesPositions, key=lambda x: (x[0], x[1]))
l = len(map[0])
total = 0
for x in range(len(map)):
    lastCube = -1
    seenRound = 0
    for index, c in enumerate(''.join(map[x])):
        if c == "#":
            total += sum(range(l-lastCube-1, l-lastCube-1-seenRound, -1))
            lastCube = index
            seenRound = 0
        elif c == "O":
            seenRound += 1
        if index == l-1:
            total += sum(range(l-lastCube-1, l-lastCube-1-seenRound, -1))

print("total = ", total)

# Part 2
