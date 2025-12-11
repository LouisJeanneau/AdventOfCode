import os
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day08_sample.txt') as f:
        data = [list(map(int, l.strip('\n').split(','))) for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day08_input.txt') as f:
        data = [list(map(int, l.strip('\n').split(','))) for l in f.readlines()]

# Part 1
answer = 0
def euclidean(a, b):
    x_a, y_a, z_a = a
    x_b, y_b, z_b = b
    return (x_b - x_a)**2 + (y_b - y_a)**2 + (z_b - z_a)**2

distances = dict()
points = len(data)
for couple in itertools.combinations(range(points), 2):
    ind_a, ind_b = couple
    a = data[ind_a]
    b = data[ind_b]
    distances[(ind_a, ind_b)] = euclidean(a, b)
distances_sorted = sorted(distances.items(), key=lambda item: item[1])

set_belonging = [-1]*points
number_connection = 10 if debug else 1000
set_belonging_free_id = 0
for connection in distances_sorted[:number_connection]:
    ind_a, ind_b = connection[0]
    set_a, set_b = set_belonging[ind_a], set_belonging[ind_b]
    if set_a == -1 and set_b == -1:
        # A or B both not in a set, create a new one
        set_belonging[ind_a] = set_belonging_free_id
        set_belonging[ind_b] = set_belonging_free_id
        set_belonging_free_id += 1
        continue
    elif set_a != -1 and set_b != -1:
        # Both in a set, we merge the sets
        set_belonging = [set_a if set_belonging[index] == set_b else set_belonging[index] for index in range(points)]
        continue    
    elif set_a == -1:
        set_belonging[ind_a] = set_b     
    else:
        set_belonging[ind_b] = set_a

set_size = sorted([set_belonging.count(i) for i in range(set_belonging_free_id)])
answer = set_size[-1] * set_size[-2] * set_size[-3]
print(f'Part 1 : {answer}')

# Part 2
answer = 0
set_belonging = [-1]*points
set_belonging_free_id = 0
for connection in distances_sorted:
    ind_a, ind_b = connection[0]
    set_a, set_b = set_belonging[ind_a], set_belonging[ind_b]
    if set_a == -1 and set_b == -1:
        # A or B both not in a set, create a new one
        set_belonging[ind_a] = set_belonging_free_id
        set_belonging[ind_b] = set_belonging_free_id
        set_belonging_free_id += 1
        continue
    elif set_a != -1 and set_b != -1:
        # Both in a set, we merge the sets
        set_belonging = [set_a if set_belonging[index] == set_b else set_belonging[index] for index in range(points)]    
    elif set_a == -1:
        set_belonging[ind_a] = set_b     
    else:
        set_belonging[ind_b] = set_a
    
    # check if we have one large set
    if set_belonging.count(set_belonging[0]) == points:
        answer = data[ind_a][0] * data[ind_b][0]
        break
print(f'Part 2 : {answer}')