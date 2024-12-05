debug = False

if debug:
    with open("2024_day05_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2024_day05_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

# Part 1
rules = []
manuals = []
first_part_input = True
for line in data:
    if line == "":
        first_part_input = False
        continue
    if first_part_input:
        rules.append([int(x) for x in line.split('|')])
    if not first_part_input:
        manuals.append([int(x) for x in line.split(',')])

ans = 0
for manual in manuals:
    valid = True
    for rule in rules:
        if rule[0] in manual and rule[1] in manual:
            if not manual.index(rule[0]) < manual.index(rule[1]):
                valid = False
                break
    if valid:
        ans += manual[len(manual) // 2]
print(f'Part 1: {ans}')