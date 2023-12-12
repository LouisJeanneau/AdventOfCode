import itertools

import numpy as np

with open("2023_day11_input.txt") as f:
# with open("2023_day11_sample.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# data = open('2023_day11_sample.txt', 'r').read()

print("input = ", data)

# Part 1
map = np.array(data)
height, width = map.shape
emptyRows = np.all(map == '.', axis=1)
emptyRows = list(np.where(emptyRows == True)[0])
emptyCols = np.all(map == '.', axis=0)
emptyCols = list(np.where(emptyCols == True)[0])
map = np.insert(map, emptyRows, ".", axis=0)
map = np.insert(map, emptyCols, ".", axis=1)
# print("map = ", map)
galaxies = np.where(map == '#')
galaxies = list(zip(galaxies[0], galaxies[1]))
totalDistance = 0
for x, y in itertools.combinations(galaxies, 2):
    # print("x = ", x, "y = ", y, "distance = ", abs(x[0]-y[0]) + abs(x[1]-y[1]))
    totalDistance += abs(x[0] - y[0]) + abs(x[1] - y[1])
print("totalDistance = ", totalDistance)

# Part 2
map = np.array(data)
galaxies = np.where(map == '#')
galaxies = list(zip(galaxies[0], galaxies[1]))
newGalaxies = []
# for x,y in galaxies:
#     t = list(np.where(emptyRows < x)[0])
#     w = list(np.where(emptyCols < y)[0])
#     a = len(t)
#     b = len(w)
#     newGalaxies.append((x + 99*a, y + 99*b))
galaxies = [(x + 999999*len(list(np.where(emptyRows < x))[0]), y + 999999*len(list(np.where(emptyCols < y))[0])) for x, y in galaxies]
totalDistance = 0
for x, y in itertools.combinations(galaxies, 2):
    # print("x = ", x, "y = ", y, "distance = ", abs(x[0]-y[0]) + abs(x[1]-y[1]))
    totalDistance += abs(x[0] - y[0]) + abs(x[1] - y[1])
print("totalDistance = ", totalDistance)
# 82
# 82
