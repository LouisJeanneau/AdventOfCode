import re
from Python.fetch_input import fetchOnline

day = 8
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

# print("input = \n", input)

# Part 1
regex1 = re.compile(r'\\\\|\\\"')
regex2 = re.compile(r'\\x[0-9a-f]{2}')
total = 0
for line in input.splitlines():
    string_literal = len(line)
    line = line[1:-1]
    string_memory = len(line) - len(regex1.findall(line)) - 3 * len(regex2.findall(line))
    # print(line, string_literal, string_memory)
    total += string_literal - string_memory
print(total)

print('---')
print("New part \n\n\n")

# Part 1 Attempt 2
total = 0
literal = 0
memory = 0
for line in input.splitlines():
    # print(line)
    literal += len(line)
    line = line[1:-1]
    while ('\\\\' in line) or ('\\\"' in line) or len(re.findall(r'\\x[0-9a-f]{2}', line)) > 0:
        line = line.replace('\\\\', '\\')
        line = line.replace('\\"', '"')
        line = re.sub(r'\\x[0-9a-f]{2}', '☺', line)
        # print(line)
    # print(line)
    memory += len(line)
print(literal, memory, literal - memory)
# 4857 is too high
# 1345 is too high
# 1266 is not good
# 1356 is not good

print('---')
print("New part \n\n\n")

# Part 1 Attempt 3
total = 0
literal = 0
memory = 0
for line in input.splitlines():
    literal += len(line)
    memory += len(eval(line))
print(literal, memory, literal - memory)


# Part 2
total = 0
for line in input.splitlines():
    total += 2 + line.count('\\') + line.count('"')
print("part 2 : ", total)
