debug = True

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
direction_start = direction

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

# Part 2
answer = 0
visited.remove(start)
for potentiel_obstacle in visited:
    i, j = start
    is_loop = False
    new_visited = set()
    new_obstacles = obstacle.copy()
    new_obstacles.add(potentiel_obstacle)
    direction = direction_start
    while 0 <= i < len(data) and 0 <= j < len(data[0]) and not is_loop:
        if (i,j, direction) in new_visited:
            is_loop = True
            break
        new_visited.add((i, j, direction))
        ni, nj = i + directions_move[direction][0], j + directions_move[direction][1]
        if (ni, nj) in new_obstacles:
            direction = (direction + 1) % 4
        else:
            i, j = ni, nj
    if is_loop:
        answer += 1
print(f'Part 2: {answer}')