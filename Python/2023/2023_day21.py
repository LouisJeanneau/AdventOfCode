from copy import deepcopy
import numpy as np

# with open("2023_day21_sample.txt") as f:
with open("2023_day21_input.txt") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
print("Part 1")
rocks = set()
start = (0, 0)
for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c == '#':
            rocks.add((x, y))
        elif c == 'S':
            start = (x, y)

# print(rocks)
height = len(data)
width = len(data[0])
positions = set()
positions.add(start)
offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(64):
    oldPositions = deepcopy(positions)
    positions.clear()
    for p in oldPositions:
        for xo, yo in offsets:
            nextX = p[0] + xo
            nextY = p[1] + yo
            if 0 <= nextX < height and 0 <= nextY < width and (nextX, nextY) not in rocks:
                positions.add((nextX, nextY))
print(len(positions))

# Part 2
print("Part 2")
positions.clear()
positions.add(start)
reachable = []
for i in range(330):
    oldPositions = deepcopy(positions)
    positions.clear()
    for p in oldPositions:
        for xo, yo in offsets:
            nextX = p[0] + xo
            nextY = p[1] + yo
            if (nextX % height, nextY % width) not in rocks:
                positions.add((nextX, nextY))
    if i == 64 or i == 64 + 131 or i == 64 + 2 * 131:
        reachable.append((i + 1, len(positions)))
print(reachable)
y = np.array([point[1] for point in reachable])
step = 26501365 // width
a = (y[0] - 2*y[1] + y[2]) / 2
b = (-3 * y[0] + 4 * y[1] - y[2]) / 2
c = y[0]
print(f"Solution : {a * (step ** 2) + b * step + c}")

# 4010704921365 too low
# 629720570456311
