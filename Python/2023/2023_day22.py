import time
import timeit
from copy import deepcopy
from typing import Tuple

# with open("2023_day22_sample.txt") as f:
with open("2023_day22_input.txt") as f:
    data = [l.strip().split("~") for l in f.readlines()]

# Part 1
print("Part 1")
data = [[[int(x) for x in coord.split(",")] for coord in line] for line in data]
# print(data)
data.sort(key=lambda x: x[0][2])
# print(data)
occupied = set()


def looseHeight(cubes: list[list[int]]) -> list[list[int]]:
    cubes[0][2] -= 1
    cubes[1][2] -= 1
    return cubes


def canFall(cubes, rocksSet: set[list[int]]):
    for p in interpolate(cubes):
        if (p[0], p[1], p[2] - 1) in rocksSet or p[2] == 1:
            return False
    return True


def interpolate(cubes: list[list[int]]) -> tuple[tuple[int, int, int], ...]:
    r = []
    for i in range(cubes[0][0], cubes[1][0] + 1):
        for j in range(cubes[0][1], cubes[1][1] + 1):
            for k in range(cubes[0][2], cubes[1][2] + 1):
                r.append((i, j, k))
    return tuple(r)


# Falling
start = time.time()
# print("time", start)
for line in data:
    while canFall(line, occupied):
        line = looseHeight(line)
    tupled = interpolate(line)
    occupied.update(tupled)
# print(occupied)
print("time", time.time() - start)

# scan
total = 0
for line in data:
    # c = deepcopy(occupied)
    inter = interpolate(line)
    for p in inter:
        occupied.remove(p)
    flag = True
    for t in [i for i in data if i[0][2] == line[1][2] + 1]:
        if not flag:
            break
        interinter = interpolate(t)
        for p in interinter:
            occupied.remove(p)
        if canFall(t, occupied):
            flag = False
        for p in interinter:
            occupied.add(p)
    # print("flag", flag, "line", line)
    for p in inter:
        occupied.add(p)
    if flag:
        total += 1
print(total)
print("time", time.time() - start)

# Part 2
# for line in data:
#     c = deepcopy(occupied)
