debug = False

if debug:
    with open("2025/2025_day03_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day03_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

# Part 1
answer = 0
for batteries_bank in data:
    batteries = list(map(int, list(batteries_bank)))
    # print(batteries)
    # Dozen unit
    dozen_position, dozen_value = 0,0
    for i, value in enumerate(batteries[:-1]):
        if value > dozen_value:
            dozen_value = value
            dozen_position = i
    # print(f'pos {dozen_position} is value {dozen_value}')
    
    # base unit
    unit_position, unit_value = 0,0
    for i, value in enumerate(batteries[dozen_position+1:]):
        if value > unit_value:
            unit_value = value
            unit_position = i
    # print(f'pos {unit_position} is value {unit_value}')
    answer += dozen_value*10 + unit_value
print(f'Part 1 : {answer}')


# Part 2
answer = 0
for batteries_bank in data:
    batteries = list(map(int, list(batteries_bank)))
    # print(batteries)
    current_digit = []
    previous_digit_position = -1
    length = len(batteries)
    for digit_rank in range(0,12):
        # rank digit        
        digit_position, digit_value = 0,0
        # print(batteries[previous_digit_position+1:length-11+digit_rank])
        for i, value in enumerate(batteries[previous_digit_position+1:length-11+digit_rank]):
            if value > digit_value:
                digit_value = value
                digit_position = i
        previous_digit_position += digit_position + 1
        current_digit.append(batteries[previous_digit_position])
        # print(f'pos {dozen_position} is value {dozen_value}')
    answer += int(''.join(map(str, current_digit)))
print(f'Part 2 : {answer}')