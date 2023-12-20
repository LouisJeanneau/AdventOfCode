import itertools
import re
import numpy as np

with open("2023_day14_input.txt") as f:
# with open("2023_day14_sample.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]


# Part 1
print("Part 1")
map = np.array(data)
map = np.rot90(map)
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
def has_cycle(lst):
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

def calculateLoadOnNorth(map:np.ndarray):
    load = 0
    max=len(map)
    for ind,l in enumerate(map):
        load += len(np.where(l=="O")[0])*(max-ind)
    return load

map = np.array(data)
modifiedMap = np.rot90(map)
total = 0
cyclesValues = []
while not has_cycle(cyclesValues):
# for _ in range(150):
    total = 0
    for i in range(4):
        map = np.array(modifiedMap)
        l = len(map[0])
        modifiedMap = np.array(map)
        modifiedMap[np.where(map == "O")] = "."
        for x in range(len(map)):
            lastCube = -1
            seenRound = 0
            for index, c in enumerate(''.join(map[x])):
                if c == "O":
                    seenRound += 1
                if c == "#" or index == len(map[0])-1:
                    r = list(range(l-lastCube-1, l-lastCube-1-seenRound, -1))
                    total += sum(r)
                    for y in range(lastCube+1, lastCube+1+seenRound):
                        modifiedMap[x,y] = "O"
                    lastCube = index
                    seenRound = 0
        # print("total = ", total)
        if i == 3:
            cyclesValues.append(calculateLoadOnNorth(np.rot90(modifiedMap, -2)))
        modifiedMap = np.rot90(modifiedMap, -1)

        # print(modifiedMap)
    # print("cycle = ", cycle, "total = ", total)
modifiedMap = np.rot90(modifiedMap, -1)
print(calculateLoadOnNorth(modifiedMap))
print(modifiedMap)


print("cyclesValues = ", cyclesValues)
# 104017 too high


