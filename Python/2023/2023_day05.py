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
        numbers = l*[-1]
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

