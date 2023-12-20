from timeit import timeit
import numpy as np

with open("2023_day18_input.txt") as f:
# with open("2023_day18_sample.txt") as f:
    data = [l.strip() for l in f.readlines()]

# Part 1
print("Part 1")
last = (0, 0)
directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
visited = set()
for line in data:
    direction, repeat, color = line.split(" ")
    repeat = int(repeat)
    for i in range(1, repeat + 1):
        x, y = last[0] + i * directions[direction][0], last[1] + i * directions[direction][1]
        visited.add((x, y))
    last = (x, y)

interior = set()
interior.add((1, 1))
while interior:
    x, y = interior.pop()
    for direction in directions.values():
        if (x + direction[0], y + direction[1]) not in visited:
            interior.add((x + direction[0], y + direction[1]))
            visited.add((x + direction[0], y + direction[1]))
# print(visited)
print(len(visited))


# Part 2
print("Part 2")

# Shoelace formula shamelessly stolen from
# https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))



directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
last = (1000000000, 1000000000)
vertex = [last]
perimeter = 0
for line in data:
    hexa = line.split(" ")[2]
    repeat = int(hexa[2:7], 16)
    direction = int(hexa[7])
    x, y = last[0] + repeat * directions[direction][0], last[1] + repeat * directions[direction][1]
    perimeter += repeat
    vertex.append((x, y))
    last = (x, y)

print("PolyArea = ", PolyArea(np.array([x[0] for x in vertex], dtype=np.int64), np.array([x[1] for x in vertex], dtype=np.int64)) + perimeter/2 + 1)
# 614143341 too low
