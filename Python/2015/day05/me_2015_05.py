from Python.fetch_input import fetchOnline

day = 5
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1
vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']
niceStrings = 0
for line in input.splitlines():
    gonext = False
    for badString in badStrings:
        if badString in line:
            gonext = True
            break
    if gonext:
        continue
    vowelCount = 0
    for vowel in vowels:
        vowelCount += line.count(vowel)
    doubleLetter = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            doubleLetter = True
            break
    if vowelCount >= 3 and doubleLetter:
        niceStrings += 1
print(niceStrings)

# Part 2
niceStringsCount = 0
for line in input.splitlines():
    doublePair = False
    for i in range(len(line) - 3):
        if line[i:i + 2] in line[i + 2:]:
            doublePair = True
            break
    if not doublePair:
        continue
    repeatLetter = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            repeatLetter = True
            break
    if repeatLetter:
        niceStringsCount += 1
print(niceStringsCount)
