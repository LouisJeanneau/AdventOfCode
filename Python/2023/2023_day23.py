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
