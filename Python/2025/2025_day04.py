import copy
debug = False

if debug:
    with open("2025/2025_day04_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day04_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

neighbours_offset = (
    (-1,-1), (-1, 0), (-1, 1), 
    (0,-1),          (0, 1),
    (1,-1),  (1, 0), (1, 1)
)

# Part 1
answer = 0
height_len = len(data)
width_len = len(data[0])
for h_pos in range(height_len):
    for w_pos in range(width_len):
        # only look around if we have a arobase
        if data[h_pos][w_pos] == '@':
            # now we check neighbours
            neighbours_arobase_count = 0
            for h_offset, w_offset in neighbours_offset:
                h_neighbour = h_pos + h_offset
                w_neighbour = w_pos + w_offset
                if 0 <= h_neighbour < height_len and \
                    0 <= w_neighbour < width_len and \
                    data[h_neighbour][w_neighbour] == '@':
                    neighbours_arobase_count += 1
            if neighbours_arobase_count < 4:
                answer+=1

print(f'Part 1: {answer}')

# Part 2
answer = 0
previous_answer = -1
data = [list(row) for row in data]
while previous_answer != answer:
    previous_answer = answer
    previous_data = copy.deepcopy(data)
    for h_pos in range(height_len):
        for w_pos in range(width_len):
            # only look around if we have a arobase
            if previous_data[h_pos][w_pos] == '@':
                # now we check neighbours
                neighbours_arobase_count = 0
                for h_offset, w_offset in neighbours_offset:
                    h_neighbour = h_pos + h_offset
                    w_neighbour = w_pos + w_offset
                    if 0 <= h_neighbour < height_len and \
                        0 <= w_neighbour < width_len and \
                        previous_data[h_neighbour][w_neighbour] == '@':
                        neighbours_arobase_count += 1
                if neighbours_arobase_count < 4:
                    answer+=1
                    data[h_pos][w_pos] = 'x'
print(f'Part 2 : {answer}')