import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day06_sample.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day06_input.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]

# Part 1
answer = 0
data_splitted = [line.split() for line in data]
height = len(data_splitted)
for column_index in range(len(data_splitted[0])):
    operation = data_splitted[-1][column_index]
    column_value = int(data_splitted[0][column_index])
    for index in range(1, height-1):
        if operation == '+':
            column_value += int(data_splitted[index][column_index])
        elif operation == '*':
            column_value *= int(data_splitted[index][column_index])
    answer += column_value
print(f'Part 1 : {answer}')

# Part 2
import numpy
answer = 0
step_value = 0
operator = ' '
data_matrix = numpy.swapaxes([list(line) for line in data], 0, 1)
for line_array in data_matrix:
    if len(''.join(line_array).strip()) == 0:
        answer += step_value
        operator = ' '
        continue
    else:
        line_value = int(''.join(line_array[:-1]))
        if operator == ' ':
            operator = line_array[-1]
            step_value = line_value
        else:
            if operator == '*':
                step_value = step_value * line_value
            elif operator == '+':
                step_value = step_value + line_value
# Don't forget the last calculation step into the total
answer += step_value
print(f'Part 2 : {answer}')