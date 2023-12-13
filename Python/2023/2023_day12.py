import re

import constraint as cstt

# with open("2023_day12_input.txt") as f:
with open("2023_day12_sample.txt") as f:
   data = [l.strip() for l in f.readlines()]

# data = open('2023_day12_sample.txt', 'r').read()

print("input = ", data)

# Part 1
for line in data:
    print(line)
    puzzle, hint = line.split(" ")
    unknowns = [ind for ind, c in enumerate(puzzle) if c == "?"]
    dots = [ind for ind, c in enumerate(puzzle) if c == "."]
    hashtags = [ind for ind, c in enumerate(puzzle) if c == "#"]
    hint = [int(i) for i in re.findall(r'\d+', hint)]
    sum_hint = sum(hint)
    problem = cstt.Problem()
    for i in range(len(puzzle)):
        problem.addVariable(i, [0, 1])
    problem.addConstraint(cstt.ExactSumConstraint(sum_hint))
    for i in dots:
        problem.addConstraint(cstt.ExactSumConstraint(0), [i])
    for i in hashtags:
        problem.addConstraint(cstt.ExactSumConstraint(1), [i])
    solutions = problem.getSolutions()
    for ind in range(len(hint)):
        valueRight = sum(hint[ind + 1:])
        valueLeft = sum(hint[:ind + 1])
        rightPart = cstt.MinSumConstraint(valueRight)
        rightRange = [i for i in range(valueLeft + ind + 1, len(puzzle))]
        if len(rightRange):
            problem.addConstraint(rightPart, rightRange)
        solutions = problem.getSolutions()

        leftPart = cstt.MaxSumConstraint(valueLeft)
        leftRange = [i for i in range(valueLeft + ind)]
        if len(leftRange):
            problem.addConstraint(leftPart, leftRange)
        solutions = problem.getSolutions()


    solutions = problem.getSolutions()
    print(len(solutions))





# Part 2
