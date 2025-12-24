from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025_day10_sample.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_day10_input.txt') as f:
        data = [l.strip('\n') for l in f.readlines()]


# Part 1
answer = 0
for line in data:
    goal = [1 if i=='#' else 0 for i in line.split("] ")[0][1:]]
    goal = np.array(goal)
    buttons = [list(map(int, i.strip("()").split(','))) for i in line.split("] ")[1].split(' ')[:-1]]

    # coefficients of the variables we want to minimize
    c = np.ones(len(buttons) + len(goal))
    c[len(buttons):] = 0

    # constraints (A @ x = b)
    A = np.zeros((len(goal), len(c)))
    for col, button_group in enumerate(buttons):
        for button in button_group:
            A[button, col] = 1
    # right part of the matrix, to do the "modulo" 2
    for index in range(len(goal)):
        A[index,-1-index] = -2
    constraints = LinearConstraint(A, lb=goal, ub=goal)
    
    # Integrality (1)
    integrality = np.full_like(c, 1)

    # Bounds (positivity)
    bounds = Bounds(lb=0, ub=np.inf)

    # Solve
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    if res.success:
        answer += res.fun
    else:
        print("Nooooooooooooo")
print()
print(f'Part 1 : {int(answer)}')

# Part 2
answer = 0


print(f'Part 2 : {answer}')