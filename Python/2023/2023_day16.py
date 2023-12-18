import numpy as np

# with open("2023_day16_sample.txt") as f:
with open("2023_day16_input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# data = open('2023_day16_sample.txt', 'r').read()

print("input = ", data)
map = np.array(data)
energised = np.zeros(map.shape, dtype=int)
beenThere = set()
toCalculate = [(0, 0, "E")]
# Part 1
print("Part 1")
# order are N E S W
effects = {'.': {'N': list((-1, 0)), 'E': list((0, 1)), 'S': list((1, 0)), 'W': list((0, -1))},
           '/': {'N': list((0, 1)), 'E': list((-1, 0)), 'S': list((0, -1)), 'W': list((1, 0))},
           '\\': {'N': ((0, -1)), 'E': ((1, 0)), 'S': ((0, 1)), 'W': ((-1, 0))},
           '|': {'N': ((-1, 0)), 'E': ((-1, 0), (1, 0)), 'S': ((1, 0)), 'W': ((-1, 0), (1, 0))},
           '-': {'N': ((0, 1), (0, -1)), 'E': ((0, 1)), 'S': ((0, 1), (0, -1)), 'W': ((0, -1))}}
translator = {(-1, 0): 'N', (0, 1): 'E', (1, 0): 'S', (0, -1): 'W'}
while len(toCalculate) != 0:
    step = toCalculate.pop()
    x, y, dir = step
    energised[x, y] = 1
    beenThere.add((x, y, dir))
    next = tuple(effects[map[x, y]][dir])
    if type(next[0]) == int:
        nextX = x + next[0]
        nextY = y + next[1]
        t = translator.get((next[0], next[1]))
        if 0 <= nextX < map.shape[0] and 0 <= nextY < map.shape[1] and (nextX, nextY, t) not in beenThere:
            toCalculate.append((nextX, nextY, t))
    else:
        for d in next:
            nextX = x + d[0]
            nextY = y + d[1]
            t = translator.get(d)
            if 0 <= nextX < map.shape[0] and 0 <= nextY < map.shape[1]  and (nextX, nextY, t) not in beenThere:
                toCalculate.append((nextX, nextY, t))
l = np.where(energised == 1)
print(len(l[0]))
print(energised)

# Part 2
print("Part 2")
