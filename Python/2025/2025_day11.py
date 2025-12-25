
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day11_sample.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day11_input.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]

# Part 1
# We're doing depth-first search with memoization
def dfs_mem(node_explored, successors_dict, value_dict: dict):
    if node_explored in value_dict:
        return value_dict.get(node_explored)
    r = 0
    for successor in successors_dict.get(node_explored):
        r += dfs_mem(successor, successors_dict, value_dict)
    value_dict[node_explored] = r
    return r

answer = 0
next_nodes = dict()
for line in data:
    current, nexts = line.split(": ")
    nexts = tuple(nexts.split(" "))
    next_nodes[current] = nexts

value_there = dict()
value_there["out"] = 1
answer = dfs_mem("you", next_nodes, value_there)
print(f'Part 1 : {answer}')

# Part 2
answer = 0


print(f'Part 2 : {answer}')