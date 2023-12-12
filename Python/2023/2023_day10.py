import numpy as np

with open("2023_day10_input.txt") as f:
# with open("2023_day10_sample.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]
# data = open('2023_day10_sample.txt', 'r').read()

print("input = ", data)
data = np.array(data)
# Part 1
directions = {"|": ((-1, 0), (1, 0)),
              "-": ((0, -1), (0, 1)),
              "L": ((-1, 0), (0, 1)),
              "J": ((-1, 0), (0, -1)),
              "7": ((0, -1), (1, 0)),
              "F": ((1, 0), (0, 1)),
              ".": ((0, 0), (0, 0))}
height = len(data)
width = len(data[0])
start = (0, 0)
# Find starting + first neighbours
start = tuple(np.where(data == "S"))
start = (start[0][0], start[1][0])
print(start)
toVisit = []
d = np.full((height, width), height*width, dtype=int)
d[start] = 1
for ind, increment in enumerate(((-1, 0), (0, 1), (1, 0), (0, -1))):
    t = tuple(np.add(start, increment))
    if data[t] in ("|7F", "-7J", "|JL", "-FL")[ind]:
        toVisit.append(t)
        d[t] = 2

while len(toVisit) != 0:
    current = toVisit.pop(0)
    for ind, increment in enumerate(directions[data[current]]):
        next = tuple(np.add(current, increment))
        c = data[current]
        if 0 <= next[0] < height and 0 <= next[1] < width and d[next] > d[current]:
            d[next] = d[current] + 1
            toVisit.append(next)

import matplotlib.pyplot as plt
d[d == height*width] = 0
plt.imshow(d, cmap="magma")
print(int(d[d == d.max()])-1)

# 281 too low
# Part 2
enclosed = 0
enclosedPointsX = []
enclosedPointsY = []
for x in range(height):
    inside = False
    prev = ""
    for y in range(width):
        if d[x, y] == 0 and inside:
            print("enclosed at ", x, y)
            enclosedPointsX.append(x)
            enclosedPointsY.append(y)
            enclosed += 1
        elif d[x, y] != 0 and data[x, y] in "|FL":
            inside = not inside
            prev = data[x, y]
        elif d[x, y] != 0 and data[x, y] in "7J":
            if (prev == "L" and data[x, y] == "J") or (prev == "F" and data[x, y] == "7"):
                inside = not inside
                prev = ""

plt.scatter(enclosedPointsY, enclosedPointsX, c="green", marker="x")
plt.show()
print(enclosed)
