import re
import itertools

# parsing de la map
symboles = set()
with open("2023_day03_input.txt") as inp:
    # pour chaque ligne
    for x, line in enumerate(inp):
        # je note la position des symbole dans un set
        for y, c in enumerate(line):
            if c in "@#&*-++=()/$%":
                symboles.add((x,y))
    # print(symboles)

total = 0
count = 0
with open("day3_input.txt") as inp:
    # je repasse sur chaque ligne
    for x, line in enumerate(inp):
        #print("caca")
        # je split la ligne pour trouver les nombres
        numbers = re.findall(r"\d+", line)
        last_y = 0
        # je trouve les positions des nombres
        for number in numbers:
            y = line[last_y:].find(number) + last_y
            last_y = y+len(number)
            #print(y)
            y_max = y+len(number)+1
            # je regarde il existe un symbole dans les positions voisines grace au set
            for couple in itertools.product( (x-1, x, x+1) , range(y-1, y_max)):
                #print(couple)
                if couple in symboles:
                    # print(number)
                    # print(couple)
                    #print(number)
                    total += int(number)
                    count += 1
                    break
    print(total)

#Part 2
print('Part 2')

height = 0
width = 0
gearsSet = set()
numbers = dict()
numberID = dict()
id = 0
with open("2023_day03_input.txt", "r") as inp:
    lines = [line.strip() for line in inp.readlines()]
    for x, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            numberID[id] = number.group()
            for y in range(number.start(), number.end()):
                numbers[(x,y)] = id
            id += 1
        for y, c in enumerate(line):
            if c in "*":
                gearsSet.add((x, y))
    #print(gearsSet)

total = 0
for x, y in gearsSet:
    ids = set()
    # We will check the 3x3 square around the gear
    for couple in itertools.product((x - 1, x, x + 1), (y - 1, y, y + 1)):
        if couple in numbers:
            ids.add(numbers[couple])
    #print(ids)
    if len(ids) == 2:
        total += int(numberID[ids.pop()]) * int(numberID[ids.pop()])

print(total)
# 81695917 too low