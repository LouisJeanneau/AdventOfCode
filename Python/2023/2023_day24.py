from sympy import symbols, Eq, solve
import itertools
import numpy as np

debug = False

if debug:
    with open("2023_day24_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2023_day24_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

data_splitted = [[[int(pos) for pos in d.split(', ')] for d in sublist.split('@')] for sublist in data]

# Part 1
ans = 0
limit_low   = 200000000000000
limit_high  = 400000000000000
if debug:
    limit_low = 7
    limit_high = 27

lines = [[data[0][0], data[0][0]+data[1][0], data[0][1], data[0][1]+data[1][1]] for data in data_splitted]
for a, b in itertools.combinations(lines, 2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    # a = x1 x2 y1 y2
    # b = x3 x4 y3 y4
    den = (a[0] - a[1]) * (b[2] - b[3]) - (a[2] - a[3]) * (b[0] - b[1])
    if den == 0:
        continue
    x = ((a[0] * a[3] - a[2] * a[1]) * (b[0] - b[1]) - (a[0] - a[1]) * (b[0] * b[3] - b[2] * b[1])) / den
    y = ((a[0] * a[3] - a[2] * a[1]) * (b[2] - b[3]) - (a[2] - a[3]) * (b[0] * b[3] - b[2] * b[1])) / den
    if limit_low <= x <= limit_high and limit_low <= y <= limit_high:
        # x = p(t) = xinit + vx * t
        # t = (x - xinit) / vx
        if (x-a[0])/(a[1]-a[0]) > 0 and (x-b[0])/(b[1]-b[0]) > 0:
            ans += 1

"""
for a, b in itertools.combinations(data_splitted, 2):
    A = np.array([[a[1][0], -b[1][0]], [a[1][1], -b[1][1]]])
    B = np.array([b[0][0] - a[0][0], b[0][1] - a[0][1]])
    try:
        # Solve the system of linear equations
        x, y = np.linalg.solve(A, B)
        print(a,b)
        print("x = ", x, "y = ", y)
        if x >= 0 and y >= 0:
            x_cross = a[0][0] + a[1][0] * x
            y_cross = a[0][1] + a[1][1] * y
            if (limit_low <= x_cross <= limit_high) and (
                    limit_low <= y_cross <= limit_high):
                ans += 1
                print("proper solution")
    except np.linalg.LinAlgError:
        continue
"""
print("Part 1 = ", ans)


# Part 2
