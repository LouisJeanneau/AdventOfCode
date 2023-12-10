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
while not finished:
   for ind, c in enumerate(current):
      current[ind] = nodes[c]["LR".index(directions[index])]
   index += 1
   count += 1
   index %= length
   if count % 100000 == 0:
      print(count)
   if ''.join( [c[-1] for c in current] ) == len(current)*"Z":
      finished = True
print(count)

