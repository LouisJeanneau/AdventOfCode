
debug = False

if debug:
    with open("2025/2025_day06_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day06_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

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
# 4487289 too low

