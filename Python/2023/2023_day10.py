with open("2023_day10_input.txt") as f:
   data = [list(l.strip()) for l in f.readlines()]
# data = open('2023_day10_sample.txt', 'r').read()

print("input = ", data)

# Part 1
directions = {"|": ((-1,0), (1,0)),
              "-": ((0,-1), (0,1)),
              "L": ((-1,0), (0,1)),
              "J": ((-1,0), (0,-1)),
              "7": ((0,-1), (1,0)),
              "F": ((1,0), (0,1)),
              ".": ((0,0), (0,0))}
height = len(data)
width = len(data[0])
s = (0,0)
# Find starting + first neighbours
for ind, line in enumerate(data):
   if line.count("S"):
      s = (ind, line.index("S"))
      break
toVisit = ((s, 0))
distances = height*[width*[-1]]
curr

print(data)

# Part 2
