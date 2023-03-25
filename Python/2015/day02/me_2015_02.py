from Python.fetch_input import fetchOnline

day = 2
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)



# Part 1
total = 0
for line in input.splitlines():
    l, w, h = map(int, line.split('x'))
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(total)

# Part 2
total = 0
for line in input.splitlines():
    l, w, h = map(int, line.split('x'))
    total += 2*min(l+w, w+h, h+l) + l*w*h
print(total)
