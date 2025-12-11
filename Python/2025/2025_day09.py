import itertools
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day09_sample.txt') as f:
        data = [list(map(int, l.strip('\n').split(','))) for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day09_input.txt') as f:
        data = [list(map(int, l.strip('\n').split(','))) for l in f.readlines()]

# Part 1
answer = 0
for corners in itertools.combinations(data, 2):
    ((x_a, y_a), (x_b, y_b)) = corners
    surface = max(x_a - x_b + 1, x_b - x_a + 1) * max(y_a - y_b + 1, y_b - y_a + 1)
    if surface > answer:
        answer = surface

print(f'Part 1 : {answer}')

# Part 2
answer = 0


print(f'Part 2 : {answer}')