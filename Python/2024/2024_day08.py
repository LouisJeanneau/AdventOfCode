from collections import defaultdict
from itertools import combinations
from math import gcd

debug = False

if debug:
    with open("2024_day08_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2024_day08_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

antennas = defaultdict(list)
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c != '.':
            antennas[c].append((i, j))
# print(antennas)

height = len(data)
width = len(data[0])
antinodes = set()
for antenna_list in antennas.values():
    for a,b in combinations(antenna_list, 2):
        diff_x, diff_y = b[0] - a[0], b[1] - a[1]
        x_a, y_a = a[0] - diff_x, a[1] - diff_y
        x_b, y_b = b[0] + diff_x, b[1] + diff_y
        if 0 <= x_a < height and 0 <= y_a < width:
            antinodes.add((x_a, y_a))
        if 0 <= x_b < height and 0 <= y_b < width:
            antinodes.add((x_b, y_b))
    # print(antenna_list)
print(f'Part 1: {len(antinodes)}')
# print(sorted(antinodes))

''' Part 2 '''
antinodes.clear()
for antenna_list in antennas.values():
    for a,b in combinations(antenna_list, 2):
        diff_x, diff_y = b[0] - a[0], b[1] - a[1]
        pgcd = gcd(diff_x, diff_y)
        diff_x /= pgcd
        diff_y /= pgcd
        iter_x, iter_y = a[0], a[1]
        while( 0 <= iter_x < height and 0 <= iter_y < width):
            antinodes.add((iter_x, iter_y))
            iter_x += diff_x
            iter_y += diff_y
        iter_x, iter_y = a[0], a[1]
        while (0 <= iter_x < height and 0 <= iter_y < width):
            antinodes.add((iter_x, iter_y))
            iter_x -= diff_x
            iter_y -= diff_y
print(f'Part 2: {len(antinodes)}')