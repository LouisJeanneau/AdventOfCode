import math
from collections import deque

# with open("2023_day23_sample.txt") as f:
with open("2023_day23_input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# Part 1
print("Part 1")
paths = set()
specials = set()
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
start = (0, 1)
end = (len(data) - 1, len(data[0]) - 2)
lengths = []

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ".":
            paths.add((i, j))
        elif data[i][j] != "#":
            specials.add((i, j))


def walk(position:tuple[int,int], visited, length):
    continueFlag = True
    while continueFlag:
        visited.add(position)
        continueFlag = False
        for index, direction in enumerate(directions):
            x = position[0] + direction[0]
            y = position[1] + direction[1]
            if (x, y) in specials and data[x][y] == "v>^<"[index]:
                walk((x,y), set(visited), length+1)
            if (x, y) in paths and (x, y) not in visited:
                length += 1
                position = (x, y)
                continueFlag = True
                break
            if position == end:
                lengths.append(length)
                return


walk(start, set(), 0)
print(lengths)
print("Answer is :", max(lengths))


# Part 2
print("Part 2")
splits = 0


def walkAgain(position:tuple[int,int], visited, length):
    global splits
    splits += 1
    # print("split at ", length)
    toVisit = deque()
    toVisit.append(position)
    while toVisit:
        position = toVisit.popleft()
        length += 1
        if position == end:
            lengths.append(length)
            print("found at ", length)
            return
        visited.add(position)
        for direction in directions:
            x = position[0] + direction[0]
            y = position[1] + direction[1]
            if (x, y) in paths and (x, y) not in visited:
                toVisit.append((x, y))
            if len(toVisit) > 1:
                walkAgain(toVisit.popleft(), set(visited), length)


lengths.clear()
paths.update(specials)
walkAgain(start, set(), -1)
print(lengths)
print("Answer is :", max(lengths))
print("Splits :", splits)
print("splits :", math.factorial(22))

