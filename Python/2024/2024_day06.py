debug = False

if debug:
    with open("2024_day06_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2024_day06_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

obstacle = set()
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == "#":
            obstacle.add((i, j))
        elif c != ".":
            start = (i, j)
            direction_char = c
direction_dict = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3
}
direction = direction_dict[direction_char]
directions_move = ((-1, 0), (0, 1), (1, 0), (0, -1))

i,j = start
visited = set()
while 0<=i<len(data) and 0<=j<len(data[0]):
    visited.add((i, j))
    ni, nj = i + directions_move[direction][0], j + directions_move[direction][1]
    if (ni, nj) in obstacle:
        direction = (direction + 1) % 4
    else:
        i, j = ni, nj
print(f'Part 1: {len(visited)}')


