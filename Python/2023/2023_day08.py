import math

with open("2023_day08_input.txt") as f:
    data = [l.strip() for l in f.readlines()]

# data = open('2023_day08_sample.txt', 'r').read()
print("input = ", data)
directions = data[0]

nodes = dict()
for line in data[2:]:
    origin, destination = line.replace("(", "").replace(")", "").split("=")
    leftDestination, rightDestination = destination.split(",")
    nodes[origin.strip()] = (leftDestination.strip(), rightDestination.strip())

print(nodes)

# Part 1
index = 0
count = 0
length = len(directions)
# current = "AAA"
# while current != "ZZZ":
#     current = nodes[current]["LR".index(directions[index])]
#     index += 1
#     count += 1
#     index %= length
# print(count)

# Part 2
index = 0
count = 0
current = [k for k in nodes.keys() if k[-1] == "A"]
print(current)
finished = False
solutions = []
while len(current) != 0:
    for ind, c in enumerate(current):
        current[ind] = nodes[c]["LR".index(directions[index])]
    count += 1
    for ind, c in enumerate(current):
        if c[-1] == "Z":
            solutions.append(count)
            current.pop(ind)
    index += 1
    index %= length
print(solutions)
print(math.lcm(*solutions))
# 326898504 too
# 1368839088 too low
# 5797723708560 too low
# 2040841573847775704247480

