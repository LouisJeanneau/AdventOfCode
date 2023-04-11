from itertools import permutations

from Python.fetch_input import fetchOnline
import numpy as np

day = 9
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)

# Part 1
# Get list of cities
cities_set = set()
for line in input.splitlines():
    splitted = line.split(' ')
    a, b = splitted[0], splitted[2]
    cities_set.add(a)
    cities_set.add(b)

dist_matrix = np.array([[10000 for x in range(len(cities_set))] for y in range(len(cities_set))])
cities = list(cities_set)
for line in input.splitlines():
    splitted = line.split(' ')
    a, b, dist = splitted[0], splitted[2], splitted[4]
    dist_matrix[cities.index(a)][cities.index(b)] = int(dist)
    dist_matrix[cities.index(b)][cities.index(a)] = int(dist)

print("cities = ", cities)
print("dist_matrix = \n", dist_matrix)

def tsp_brute_force(dist_matrix):
    shortest_dist = 100000
    shortest_path = []
    for path in permutations(range(len(dist_matrix[0]))):
        dist = sum( dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1) )
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = path
    return shortest_dist, shortest_path

print("tsp_brute_force = ", tsp_brute_force(dist_matrix)[0])
print("tsp_brute_force = ", tsp_brute_force(dist_matrix)[1])
# Part 2
