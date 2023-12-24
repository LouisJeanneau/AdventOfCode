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


def has_cycle(lst):
    if len(lst) < 150:
        return False
    tortoise = hare = 0
    try:
        while True:
            tortoise += 1
            hare += 2

            if lst[tortoise] == lst[hare]:
                return True  # Cycle detected

            if hare is None or lst[hare] is None:
                return False  # No cycle
    except IndexError:
        return False


positions.clear()
positions.add(start)
reachable = []
diff = []
# maps = set()
i = -1
# while not has_cycle(diff):
for i in range(330):
    # i+=1
    oldPositions = deepcopy(positions)
    positions.clear()
    for p in oldPositions:
        for xo, yo in offsets:
            nextX = p[0] + xo
            nextY = p[1] + yo
            # maps.add((nextX // height, nextY // width))
            if (nextX % height, nextY % width) not in rocks:
                positions.add((nextX, nextY))
    # print(f"i = {i} and len = {len(positions)}")
    # reachable.append((len(positions), len(maps)))
    # if i!=0:
    #     diff.append(reachable[-1] - reachable[-2])
    if i == 64 or i == 64 + 131 or i == 64 + 2 * 131:
        reachable.append((i + 1, len(positions)))
print(reachable)
x = np.array([point[0] for point in reachable])
step = 26501365 // width
a = (x[0] - x[1] + x[2]) / 2
b = (-3 * x[0] + 4 * x[1] - x[2]) / 2
c = x[0]
print(f"Solution : {a * (step ** 2) + b * step + c}")

# y = np.array([point[1] for point in reachable])
#
# # Form the matrix A for the system of equations
# A = np.vstack([x ** 2, x, np.ones(len(x))]).T
#
# # Solve for coefficients a, b, and c
# coefficients = np.polyfit(x,y, 2)
# print(coefficients)
# # Coefficients will be in the order [a, b, c]
# a, b, c = coefficients
# step = 26501365
# # print(diff)

# 4010704921365 too low
# 36695019340
