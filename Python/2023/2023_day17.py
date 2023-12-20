import numpy as np
import heapq

# with open("2023_day17_input.txt") as f:
with open("2023_day17_sample.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# data = open('2023_day17_sample.txt', 'r').read()

print("input = ", data)

# Part 1
map = np.array([[int(i) for i in line] for line in data])


def dijkstra_2d_array_limit_directions(cost_matrix, start, pointingStart):
    rows, cols = cost_matrix.shape
    visited = np.zeros((rows, cols, 4), dtype=bool)
    distances = np.full((rows, cols, 4), np.inf)
    distances[start] = 0

    heap = [(0, start, pointingStart)]

    while heap:
        current_dist, current_node, bannedDirection = heapq.heappop(heap)

        # if visited[current_node][bannedDirection]:
        #     continue

        visited[current_node, bannedDirection] = True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            if direction == directions[bannedDirection]:  # or direction == directions[bannedDirection-2]:
                continue
            intermediate = 0
            for mult in range(1, 4):  # Limit to three consecutive times in a direction
                n_row, n_col = current_node[0] + mult * direction[0], current_node[1] + mult * direction[1]

                if 0 <= n_row < rows and 0 <= n_col < cols:
                    new_distance = current_dist + intermediate + cost_matrix[n_row, n_col]
                    intermediate += cost_matrix[n_row, n_col]
                    if new_distance <= distances[n_row, n_col, directions.index(direction)]:
                        distances[(n_row, n_col, directions.index(direction))] = new_distance
                        heapq.heappush(heap, (new_distance, (n_row, n_col), directions.index(direction)))

                else:
                    break  # Stop exploring if out of bounds

    return distances


# Example usage:
start_node = (0, 0)
result = dijkstra_2d_array_limit_directions(map, start_node, 2)
# print(result)
print(result[-1, -1, :])


# 1014 too high

# Part 2
def dijkstra_2d_array_limit_directions_ultra(cost_matrix, start, pointingStart):
    rows, cols = cost_matrix.shape
    visited = np.zeros((rows, cols, 4), dtype=bool)
    distances = np.full((rows, cols, 4), np.inf)
    distances[start] = 0

    heap = [(0, start, pointingStart)]

    while heap:
        current_dist, current_node, bannedDirection = heapq.heappop(heap)

        # if visited[current_node][bannedDirection]:
        #     continue

        visited[current_node, bannedDirection] = True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            if direction == directions[bannedDirection]:  # or direction == directions[bannedDirection-2]:
                continue
            intermediate = 0
            for mult in range(10):  # Limit to three consecutive times in a direction
                n_row, n_col = current_node[0] + (mult + 1) * direction[0], current_node[1] + (mult + 1) * direction[1]

                if 0 <= n_row < rows and 0 <= n_col < cols:
                    new_distance = current_dist + intermediate + cost_matrix[n_row, n_col]
                    intermediate += cost_matrix[n_row, n_col]
                    if mult > 3 and new_distance <= distances[n_row, n_col, directions.index(direction)]:
                        distances[(n_row, n_col, directions.index(direction))] = new_distance
                        heapq.heappush(heap, (new_distance, (n_row, n_col), directions.index(direction)))

                else:
                    break  # Stop exploring if out of bounds

    return distances


start_node = (0, 0)
result = dijkstra_2d_array_limit_directions_ultra(map, start_node, 2)
# print(result)
print(result[-1, -1, :])
