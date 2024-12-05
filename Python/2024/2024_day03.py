import re

debug = False

if debug:
    with open("2024_day03_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2024_day03_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

ans = 0
regex_mul = re.compile("mul\(\d{1,3},\d{1,3}\)")
regex_int = re.compile("\d{1,3}")
for line in data:
    if regex_mul.search(line):
        for m in regex_mul.findall(line):
            a, b = map(int, regex_int.findall(m))
            ans += a * b
print(f'Part 1 : {ans}')

# Part 2
ans = 0
regex_do = re.compile("do\(\)")
regex_dont = re.compile("don't\(\)")
line = ''.join(data)
for m in re.finditer("mul\(\d{1,3},\d{1,3}\)", line):
    sub = line[0:m.start()]
    do_index = [m.end() for m in regex_do.finditer(sub)]
    dont_index = [m.end() for m in regex_dont.finditer(sub)]
    # print(m.end())
    if len(dont_index) != 0 and (len(do_index) == 0 or dont_index[-1] > do_index[-1]):
        continue
    a, b = map(int, regex_int.findall(m.group()))
    ans += a * b
print(f'Part 2 : {ans}')
# 94810037 too high
