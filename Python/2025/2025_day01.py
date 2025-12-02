
debug = False

if debug:
    with open("2025/2025_day01_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day01_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

# Part 1
dial_position = 50
answer = 0

for rotation in data:
    offset = int(str(rotation[1:]))
    dial_position = dial_position - offset if 'L' in rotation else dial_position + offset
    dial_position %= 100
    answer += dial_position == 0

print(f'The answer is {answer}\n')

# Part 2
dial_position = 50
answer = 0

for rotation in data:
    offset = int(str(rotation[1:]))
    # il faut compter seulement quand ON PASSE OU S'ARRETE SUR 0
    if 'L' in rotation:
        for i in range(offset):
            dial_position-=1
            if dial_position == 0:
                answer += 1
            elif dial_position == -1:
                dial_position = 99
    else:
        for i in range(offset):
            dial_position+=1
            if dial_position == 100:
                answer += 1
                dial_position = 0


print(f'The answer of part 2 is {answer}')
