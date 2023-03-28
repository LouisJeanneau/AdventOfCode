from Python.fetch_input import fetchOnline

day = 7
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1 - tried something with eval, but it is unnecessarily complicated
lines = input.splitlines()
wires = {}
replace = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}
for line in lines:
    for key in replace:
        line = line.replace(key, replace[key])
    values = line.split(" -> ")
    wires[values[1]] = values[0]

def evalWire(wire: str):
    # print("wire = ", wire)
    if wire.isdigit():
        return int(wire)
    if type(wires[wire]) == int:
        return int(wires[wire])
    elif type(wires[wire]) == int:
        return wires[wire]
    to_eval = wires[wire].split(" ")
    # print("to_eval = ", to_eval)
    if len(to_eval) == 1:
        return evalWire(to_eval[0])
    elif len(to_eval) == 2:
        return ~evalWire(to_eval[1])
    elif len(to_eval) == 3:
        evalWire(to_eval[0])
        evalWire(to_eval[2])
        v0 = evalWire(to_eval[0])
        v1 = evalWire(to_eval[2])
        # print(f'dealing with {v0} {to_eval[1]} {v1}')
        # print(eval(f'{v0} {to_eval[1]} {v1}'))
        wires[wire] = eval(f'{v0} {to_eval[1]} {v1}')
        return wires[wire]

solution = evalWire('a')
print(solution)

# Part 1 bis - tried something else - didn't work
'''
operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']
wires.clear()
for line in lines:
    values = line.split(" -> ")
    wires[values[1]] = values[0]

def getWireValue(wire):
    print("wire = ", wire)
    if wire.isdigit():
        return int(wire)
    if wires[wire].isdigit():
        print(f'wires[{wire}] = {wires[wire]}')
        return int(wires[wire])
    to_eval = wires[wire].split(" ")
    print("to_eval = ", to_eval)
    if len(to_eval) == 1:
        return getWireValue(to_eval[0])
    for op in operators:
        if op in to_eval:
            if op == 'AND':
                return getWireValue(to_eval[0]) & getWireValue(to_eval[2])
            if op == 'OR':
                return getWireValue(to_eval[0]) | getWireValue(to_eval[2])
            if op == 'LSHIFT':
                return getWireValue(to_eval[0]) << getWireValue(to_eval[2])
            if op == 'RSHIFT':
                return getWireValue(to_eval[0]) >> getWireValue(to_eval[2])
            if op == 'NOT':
                return ~getWireValue(to_eval[1])

print(getWireValue('a'))
'''

# Part 2
wires.clear()
for line in lines:
    for key in replace:
        line = line.replace(key, replace[key])
    values = line.split(" -> ")
    wires[values[1]] = values[0]
wires['b'] = solution
print(evalWire('a'))
