from Python.fetch_input import fetchOnline

day = 1
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()
print("input = ", input)
# Part 1
print(input.count('(') - input.count(')'), "floor")
# Part 2
floor = 0
for i in range(len(input)):
    if input[i] == '(':
        floor += 1
    elif input[i] == ')':
        floor -= 1
    if floor == -1:
        print(i + 1)
        break