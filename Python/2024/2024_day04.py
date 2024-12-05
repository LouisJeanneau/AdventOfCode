import pandas as pd
from typing import Tuple

debug = True

if debug:
    with open("2024_day04_sample.txt") as f:
        data = [list(l.strip()) for l in f.readlines()]
else:
    with open("2024_day04_input.txt") as f:
        data = [list(l.strip()) for l in f.readlines()]

mat = pd.DataFrame(data)

word = "XMAS"
rows, cols = mat.shape
word_len = len(word)

# Define directions
directions = [
    (0, 1),   # Horizontal right
    (1, 0),   # Vertical down
    (0, -1),  # Horizontal left
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down-right
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
    (-1, -1)  # Diagonal up-left
]

def is_word_in_direction(start: Tuple[int, int], direction: Tuple[int, int]) -> bool:
    """Check if the word exists starting from 'start' in 'direction'."""
    x, y = start
    dx, dy = direction
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        # Check bounds and character match
        if not (0 <= nx < rows and 0 <= ny < cols) or mat.iloc[nx, ny] != word[i]:
            return False
    return True

# Count occurrences
count = 0
for x in range(rows):
    for y in range(cols):
        for direction in directions:
            if is_word_in_direction((x, y), direction):
                count += 1
print(f'Part 1: {count}')