with open("2023_day05_input.txt") as f:
    data = [l.strip() for l in f.readlines()]
    data.append(" ")

# Part 1
numbers = [int(i) for i in data[0].split(":")[1].strip().split(" ")]
old_numbers = numbers.copy()
l = len(numbers)
print(numbers)
transfers = dict()

for x, line in enumerate(data[3:]):
    if len(line.strip()) == 0:
        old_numbers = numbers.copy()
        numbers = l * [-1]
        for index, number in enumerate(old_numbers):
            for transfer in transfers.items():
                if transfer[0][0] <= number <= transfer[0][1]:
                    numbers[index] = number + transfer[1]
                    break
                numbers[index] = number
        continue

    if line.find("map") != -1:
        transfers.clear()
        continue

    dst, src, ran = line.strip().split(" ")
    dst = int(dst)
    src = int(src)
    ran = int(ran)
    transfers[(src, src + ran - 1)] = dst - src
print(min(numbers))

# Part 2
# Damn
seeds = [int(i) for i in data[0].split(":")[1].strip().split(" ")]
seeds_range = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

maps = []
current_map = []
for x, line in enumerate(data[3:]):
    if len(line.strip()) == 0:
        maps.append(current_map.copy())
        continue

    if line.find("map") != -1:
        current_map.clear()
        continue

    dst, src, ran = line.strip().split(" ")
    dst = int(dst)
    src = int(src)
    ran = int(ran)
    current_map.append(((src, src + ran - 1), dst - src))

# Now we start
for i in range(len(maps)):
    current_map = maps[i]
    current_map.sort(key=lambda x: x[0])
    old_range = seeds_range.copy()
    old_range.sort(key=lambda x: x[0])
    minmin = min(current_map[0][0][0], old_range[0][0])
    maxmax = max(current_map[-1][0][1], old_range[-1][1])
    current_map.insert(0, ((0, minmin - 1), 0))
    current_map.append( ((maxmax + 1, 1000000), 0) )
    print(current_map)
    missing = []
    for i in range(1, len(current_map)):
        if current_map[i][0][0] - current_map[i-1][0][1] > 1:
            missing.append( ((current_map[i-1][0][1]+1, current_map[i][0][0]-1), 0) )
    current_map.extend(missing)
    current_map.sort(key=lambda x: x[0])
    print(current_map)
    seeds_range = []
    for ran in old_range:
        for transfer in current_map:
            # intersect ran and transfer :
            if len(range(max(ran[0], transfer[0][0]), min(ran[1], transfer[0][1]))) != 0:
                seeds_range.append(
                    (max(ran[0], transfer[0][0]) + transfer[1], min(ran[1], transfer[0][1]) + transfer[1]))
print(seeds_range)
print(min([min(ran) for ran in seeds_range]))

# 66405002 too high
