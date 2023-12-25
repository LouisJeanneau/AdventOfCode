from copy import deepcopy

# with open("2023_day22_sample.txt") as f:
with open("2023_day22_input.txt") as f:
    data = [l.strip().split("~") for l in f.readlines()]

# Part 1
print("Part 1")
data = [[[int(x) for x in coord.split(",")] for coord in line] for line in data]
print(data)
data.sort(key=lambda x: x[0][2])
print(data)
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


def interpolate(cubes: list[list[int]]) -> tuple[list[int]]:
    r = []
    for i in range(cubes[0][0], cubes[1][0] + 1):
        for j in range(cubes[0][1], cubes[1][1] + 1):
            for k in range(cubes[0][2], cubes[1][2] + 1):
                r.append([i, j, k])
    return tuple(r)


# Falling
for line in data:
    while canFall(line, occupied):
        line = looseHeight(line)
    tupled = tuple([tuple(i) for i in interpolate(line)])
    occupied.update(tupled)
print(occupied)

# scan
total = 0
for line in data:
    c = deepcopy(occupied)
    for p in interpolate(line):
        if tuple(p) in c:
            c.remove(tuple(p))
    flag = True
    for t in [i for i in data if i[0][2] == line[1][2] + 1]:
        d = deepcopy(c)
        for p in interpolate(t):
            if tuple(p) in d:
                d.remove(tuple(p))
        if canFall(t, d):
            flag = False
            break
    print("flag", flag, "line", line)
    if flag:
        total += 1
print(total)

# Part 2
