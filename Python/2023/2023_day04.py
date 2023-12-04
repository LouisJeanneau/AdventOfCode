import re

with open("2023_day04_input.txt") as f:
    data = [l.strip() for l in f.readlines()]
total = 0
for line in data:
    left, right = line.split("|")
    winning = left.split(":")[1].strip()
    winningNumbers = re.findall(r'\d+', winning)
    winningNumbers = [int(i) for i in winningNumbers]
    draw = re.findall(r'\d+', right)
    draw = [int(i) for i in draw]
    common = set(winningNumbers) & set(draw)
    if len(common) != 0:
        total += 1<<(len(common)-1)
print(total)

# Part 2
counts = len(data)*[1]
for x, line in enumerate(data):
    left, right = line.split("|")
    winning = left.split(":")[1].strip()
    winningNumbers = re.findall(r'\d+', winning)
    winningNumbers = [int(i) for i in winningNumbers]
    draw = re.findall(r'\d+', right)
    draw = [int(i) for i in draw]
    common = set(winningNumbers) & set(draw)
    for i in range(len(common)):
        if x+i+1 < len(counts):
            counts[x+i+1] = counts[x+i+1] + counts[x]
print(sum(counts))