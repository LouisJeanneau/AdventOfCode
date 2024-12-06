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

correct_manuals = []
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
        correct_manuals.append(manual)
print(f'Part 1: {ans}')

# Part 2
ans = 0
for manual in correct_manuals:
    manuals.remove(manual)

for manual in manuals:
    valid = False
    while not valid:
        restart = False
        for i in range(len(manual) - 1):
            for rule in rules:
                if rule[0] in manual[i:i+2] and rule[1] in manual[i:i+2]:
                    if manual[i]==rule[1] and manual[i+1]==rule[0]:
                        manual[i], manual[i+1] = manual[i+1], manual[i]
                        restart = True
                        break
            if restart:
                break
        if not restart:
            valid = True
    ans += manual[len(manual) // 2]
print(f'Part 2: {ans}')