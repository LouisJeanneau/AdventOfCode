import re
with open("2023_day19_input.txt") as f:
# with open("2023_day19_sample.txt") as f:
   data = [l.strip() for l in f.readlines()]

# Part 1
print("Part 1")
instructionsText = data[0:data.index('')]
instructions = {}
for instruction in instructionsText:
    print(instruction)
    label = re.findall(r'^[a-z]+', instruction)[0]
    comparaisons = re.findall(r'\{.+\}', instruction)[0][1:-1].split(',')
    comparaisons = [c.split(':') for c in comparaisons]
    print(label)
    print(comparaisons)
    instructions[label] = comparaisons

total = 0
for element in data[data.index('') + 1:]:
    print(element)
    x,m,a,s = [int(i) for i in re.findall(r'\d+', element)]
    print(x,m,a,s)
    finished = False
    lab = "in"
    while not finished:
        if lab == "A":
            total += x + m + a + s
            finished = True
            break
        if lab == "R":
            finished = True
            break
        for instruction in instructions[lab]:
            if len(instruction) == 1:
                lab = instruction[0]
            elif eval(instruction[0]):
                lab = instruction[1]
                break

print("total = ", total)

# Part 2
print("Part 2")

