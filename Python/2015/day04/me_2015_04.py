import hashlib

from Python.fetch_input import fetchOnline

day = 4
input = fetchOnline(2015, day)
input = input.strip()
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1 + 2
i = 0
while True:
    i += 1
    h = hashlib.md5((input + str(i)).encode('utf')).hexdigest()
    # choose the first 5 or 6 zeros
    if h.startswith('000000'):
        print(h, i)
        break
print(i)

# Part 2

