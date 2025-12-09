import copy
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day07_sample.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day07_input.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]

# Part 1
answer = 0
tachyon_set_next = set()
tachyon_set_next.add(data[0].find('S'))
line_length = len(data[0])

for line in data[2::2]:
    tachyon_set_previous = copy.deepcopy(tachyon_set_next)
    tachyon_set_next.clear()
    for tachyon_pos in tachyon_set_previous:
        if line[tachyon_pos] == '^':
            answer += 1
            if tachyon_pos > 0:
                tachyon_set_next.add(tachyon_pos-1)
            if tachyon_pos < line_length-1:
                tachyon_set_next.add(tachyon_pos+1)
        else:
            tachyon_set_next.add(tachyon_pos)  

print(f'Part 1 : {answer}')

# Part 2
answer = 0
start_y = data[0].find('S')

def explore(map_2d, position, cache: dict):
    x, y = position
    if position in cache:
        return cache[position]
    elif x >= len(map_2d):
        return 1
    elif map_2d[x][y] == '^':
        res = explore(map_2d, (x+1,y-1), cache) + explore(map_2d, (x+1,y+1), cache)
        cache[(x,y)] = res
        return res
    else:
        res = explore(map_2d, (x+1,y), cache)
        cache[(x,y)] = res
        return res

map_2d = data[2::2]
cache_2d = dict()
answer = explore(map_2d, (0, start_y), cache_2d)

print(f'Part 2 : {answer}')