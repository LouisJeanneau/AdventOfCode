from Python.fetch_input import fetchOnline

day = 3
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1
visited = set()
x = y = 0
visited.add((x, y))
for char in input:
    if char == '<':
        x -= 1
    elif char == '>':
        x += 1
    elif char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    visited.add((x, y))
print(len(visited))

# Part 2
visited = set()
x = y = j = k = 0
visited.add((x, y))
for i, char in enumerate(input):
    if i % 2 == 0:
        if char == '<':
            x -= 1
        elif char == '>':
            x += 1
        elif char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        visited.add((x, y))
    else:
        if char == '<':
            j -= 1
        elif char == '>':
            j += 1
        elif char == '^':
            k += 1
        elif char == 'v':
            k -= 1
        visited.add((j, k))
print(len(visited))