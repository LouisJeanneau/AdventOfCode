
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day12_sample.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day12_input.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]

# Part 1
answer = 0
# assume all 6 shapes are 3x3 square, so ignore in the parsing
skip_shapes = 6 * 5
trees = data[skip_shapes:]
for tree in trees:
    surface = int(tree[0:2]) * int(tree[3:5])
    boxes = sum([int(i) for i in tree[7:].split(' ')])
    if boxes <= surface / 9:
        answer += 1
print(f'Part 1 : {answer}')

# Part 2
answer = 0


print(f'Part 2 : {answer}')