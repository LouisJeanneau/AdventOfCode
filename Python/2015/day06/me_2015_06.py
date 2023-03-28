from Python.fetch_input import fetchOnline

day = 6
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1
lights_on = set()
for line in input.splitlines():
    x,y = map(int, line.split(' ')[-3].split(','))
    x2,y2 = map(int, line.split(' ')[-1].split(','))
    for i in range(x, x2 + 1):
        for j in range(y, y2 + 1):
            if line.startswith('turn on'):
                lights_on.add((i,j))
            elif line.startswith('turn off'):
                lights_on.discard((i,j))
            elif line.startswith('toggle'):
                if (i,j) in lights_on:
                    lights_on.discard((i,j))
                else:
                    lights_on.add((i,j))
print(len(lights_on))

# Part 2
lights_brightness = {}
for line in input.splitlines():
    x,y = map(int, line.split(' ')[-3].split(','))
    x2,y2 = map(int, line.split(' ')[-1].split(','))
    for i in range(x, x2 + 1):
        for j in range(y, y2 + 1):
            if line.startswith('turn on'):
                lights_brightness[(i,j)] = lights_brightness.get((i,j), 0) + 1
            elif line.startswith('turn off'):
                lights_brightness[(i,j)] = max(0, lights_brightness.get((i,j), 0) - 1)
            elif line.startswith('toggle'):
                lights_brightness[(i,j)] = lights_brightness.get((i,j), 0) + 2
print(sum(lights_brightness.values()))