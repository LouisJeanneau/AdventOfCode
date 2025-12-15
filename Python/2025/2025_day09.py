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
import numpy
import sys
answer = 0
data.append(data[0])
height = max(map(lambda x: x[0], data)) + 2
width = max(map(lambda x: x[1], data)) + 2
matrix = numpy.ones((height, width), bool)
print(f'size is {sys.getsizeof(matrix)}')
for (x_a, y_a), (x_b, y_b) in zip(data[:-1], data[1:]):
    if x_b < x_a:
        x_a, x_b = x_b, x_a
    elif y_b < y_a:
        y_a, y_b = y_b, y_a
    
    for x_todraw in range(x_a, x_b + 1):
        for y_todraw in range(y_a, y_b + 1):
            matrix[x_todraw, y_todraw] = False
print(f'size is {sys.getsizeof(matrix)}')
matrix_border = numpy.copy(matrix)

# fill the contour
queue_to_color = set()
queue_to_color.add((0,0))
offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
while queue_to_color:
    position = queue_to_color.pop()
    for x, y in [(position[0] + offset[0], position[1] + offset[1]) for offset in offsets]:
        if x < 0 or x >= height or y < 0 or y >= width:
            continue
        if matrix[x,y] == False:
            continue
        queue_to_color.add((x,y))
    matrix[position] = False
res = matrix + ~matrix_border

for (x_a, y_a), (x_b, y_b) in itertools.combinations(data[:-1], 2):
    if x_b < x_a:
        x_a, x_b = x_b, x_a
    if y_b < y_a:
        y_a, y_b = y_b, y_a
    surface = (x_b - x_a + 1) * (y_b - y_a + 1)
    trues = numpy.count_nonzero(res[x_a:x_b + 1, y_a:y_b + 1])
    if surface == trues:
        if surface > answer:
            answer = surface


# import matplotlib.pyplot as plt
# plt.figure(figsize=(6, 6))
# plt.imshow(res, cmap='binary', origin='lower')
# plt.show()
print(f'Part 2 : {answer}')