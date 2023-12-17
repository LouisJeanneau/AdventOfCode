import re
import numpy as np

# with open("2023_day14_input.txt") as f:
with open("2023_day14_sample.txt") as f:
   data = [list(l.strip()) for l in f.readlines()]

# data = open('2023_day14_sample.txt', 'r').read()

print("input = ", data)

# Part 1
print("Part 1")
map = np.array(data)
map = map.T
cubes = np.where(map == '#')
l = len(map)
cubesPositions = [(i, l+1) for i in range(l)]
cubesPositions.extend(list(zip(cubes[0], cubes[1])))
seen = set()
cubesPositions = sorted(cubesPositions, key=lambda x: (x[0], x[1]))
cubesPositions = [y for x,y in cubesPositions if not x in seen and not seen.add(x)]
rollingStones = []
for x in range(len(map)):
   rollingStones.append(sum([len(i) for i in re.findall(r'O+', ''.join(map[x])[:cubesPositions[x]])]))
print(sum([sum([j for j in range(l,l-i, -1)]) for i in rollingStones]))


# Part 2
