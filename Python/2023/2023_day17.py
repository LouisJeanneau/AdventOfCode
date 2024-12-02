import numpy as np
import heapq


with open("2023_day17_input.txt") as f:
# with open("2023_day17_sample1.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

# Part 1
map = np.array([[int(i) for i in line] for line in data])
def dijkstra_2d_array_limit_directions(cost_matrix, start, pointingStart):
    rows, cols = cost_matrix.shape
    visited = np.zeros((rows, cols, 4), dtype=bool)
    distances = np.full((rows, cols, 4), np.inf)
    distances[start] = 0

    heap = [(0, start, pointingStart)]
    i=0
    while heap:
        i+=1
        if i==50000:
            print(current_node)
            print(len(heap))
            i=0
        current_dist, current_node, bannedDirection = heapq.heappop(heap)

        # if visited[current_node][bannedDirection]:
        #     continue

        visited[current_node, bannedDirection] = True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            if (direction == directions[bannedDirection] or direction == directions[(bannedDirection+2)%4]) and current_dist!=0:
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

# Part 2
def find_path(cost_matrix):
    # (total_cost, position, direction, straight_moves)
    start_states = [
            (0, (0, 0), (0, 1), 0),  # starting right
            (0, (0, 0), (1, 0), 0)   # starting down
        ]
    open_set = start_states
    rows, cols = cost_matrix.shape
    target = (rows - 1, cols - 1)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track minimum costs to reach each state
    visited = {}
    
    while open_set:
        total_cost, current, prev_dir, straight_moves = heapq.heappop(open_set)
        
        # Reached target
        if current == target and straight_moves >= 4:
            return total_cost
        
        # State key to prevent redundant explorations
        state_key = (current, prev_dir, straight_moves)
        
        # Skip if we've found a cheaper path to this state
        if state_key in visited and visited[state_key] <= total_cost:
            continue
        visited[state_key] = total_cost
        
        # Explore neighbors
        for new_dir in directions:
            # Can't turn around
            if prev_dir and (new_dir[0] == -prev_dir[0] and new_dir[1] == -prev_dir[1]):
                continue
            
            # Determine straight move count
            new_straight_moves = (straight_moves + 1) if new_dir == prev_dir else 1
            
            # Enforce straight move constraints
            if new_straight_moves > 10 or (prev_dir and new_dir != prev_dir and straight_moves < 4):
                continue
            
            # Calculate new position
            new_pos = (current[0] + new_dir[0], current[1] + new_dir[1])
            
            # Validate new position
            if not (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols):
                continue
            
            # Calculate new total cost
            new_total_cost = total_cost + cost_matrix[new_pos[0]][new_pos[1]]
            
            # Add to open set
            heapq.heappush(open_set, (
                new_total_cost, 
                new_pos, 
                new_dir, 
                new_straight_moves
            ))
    
    return None  # No path found

start_node = (0, 0)

# print(result[-1, -1, :])
result = find_path(map)
print(result)


