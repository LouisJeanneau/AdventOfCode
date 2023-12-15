import numpy as np

# with open("2023_day13_sample.txt") as f:
with open("2023_day13_input.txt") as f:
    data = [l.strip() for l in f.readlines()]
    data.append("")

# data = open('2023_day13_sample.txt', 'r').read()

print("input = ", data)
def scan(map, useSmudge):
    for x in range(1, len(map)):
        cont = True
        smudgeFound = not useSmudge
        for i in range(x):
            if 0 <= x - 1 - i < len(map) and 0 <= x + i < len(map):
                t = np.equal(map[x - 1 - i,], map[x + i,])
                c = len(np.where(t == False)[0])
                if c == 1 and not smudgeFound:
                    current = map[x - 1 - i,np.where(t == False)[0][0]]
                    #map[x - 1 - i,np.where(t == False)[0][0]] = "#."[".#".index(current)]
                    smudgeFound = True
                elif np.any(np.not_equal(map[x - 1 - i,], map[x + i,])):
                    cont = False
                    break
            else:
                break
        if cont and smudgeFound:
            return x
    return 0


# Part 1
startMap = 0
total = 0
mapCount = 0
while data[startMap:].count(""):
    # mapCount += 1
    # print("mapCount = ", mapCount)
    endMap = data[startMap:].index("") + startMap
    map = data[startMap:endMap]
    map = np.array([list(r) for r in map])
    startMap = endMap + 1
    # vertical scan
    total += 100 * scan(map, False)

    map = map.T
    # horizontal scan
    total += scan(map, False)
print("total =", total)
# 35299 too high

# Part 2
print("Part 2")
startMap = 0
total = 0
mapCount = 0
while data[startMap:].count(""):
    # mapCount += 1
    # print("mapCount = ", mapCount)
    endMap = data[startMap:].index("") + startMap
    map = data[startMap:endMap]
    map = np.array([list(r) for r in map])
    startMap = endMap + 1

    # scan up to down
    total += 100 * scan(map, True)

    # scan left to right
    map = map.T
    total += scan(map, True)
print("total =", total)
# 48200 too high
# 38894 too high
