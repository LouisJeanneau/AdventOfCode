debug = False

if debug:
    with open("2024_day07_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2024_day07_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

data_formatted = []
for line in data:
    left, right = line.split(": ")
    left = int(left)
    right = tuple(map(int, right.split(' ')))
    data_formatted.append((left, right))
print(data_formatted)

def cycle(goal: int, numbers: tuple):
    # End of cycle
    if len(numbers) == 1:
        if numbers[0] == goal:
            return True
        else:
            return False
    # Go deeper on the list
    elif goal % numbers[-1] == 0:
        return cycle(goal//numbers[-1], numbers[:-1]) or cycle(goal-numbers[-1], numbers[:-1])
    else:
        return cycle(goal-numbers[-1], numbers[:-1])

answer = 0
for line in data_formatted:
    answer += line[0] * cycle(line[0], line[1])
print(f'Part 1: {answer}')

# Part 2
def cycle_part_two(goal: int, numbers: tuple):
    # End of cycle
    if goal <= 0:
        return False
    elif len(numbers) == 1:
        if numbers[0] == goal:
            return True
        else:
            return False
    # Go deeper on the list
    next_cycle = []
    numbers_next_step = numbers[:-1]
    # Addition
    next_cycle.append( cycle_part_two(goal-numbers[-1], numbers_next_step) )
    # Multiplication
    if goal % numbers[-1] == 0:
        next_cycle.append( cycle_part_two(goal//numbers[-1], numbers_next_step) )
    # Concatenation
    number_string = str(numbers[-1])
    if str(goal)[-(len(number_string)):] == number_string:
        if len(number_string) != len(str(goal)):
            goal_next_step = int( str(goal)[:-(len(number_string))] )
            next_cycle.append( cycle_part_two(goal_next_step, numbers_next_step))
    return any(next_cycle)

answer = 0
for line in data_formatted:
    answer += line[0] * cycle_part_two(line[0], line[1])
print(f'Part 2: {answer}')