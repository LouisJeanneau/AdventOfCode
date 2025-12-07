import pandas as pd
debug = False

if debug:
    with open("2025/2025_day05_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day05_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

# Part 1
answer = 0
fresh_interval_set = set()
index = 0
while data[index] != "":
    left, right = map(int, data[index].split('-'))
    fresh_interval_set.add(pd.Interval(left, right, closed='both'))
    index += 1

index += 1
for ingredient in data[index:]:
    ingredient_id = int(ingredient)
    for fresh_range in fresh_interval_set:
        if ingredient_id in fresh_range:
            answer+=1
            break
print(f'Part 1 : {answer}')

# Part 2
import portion
answer = 0
index = 0
new_fresh_interval_set = portion.empty()
while data[index] != "":
    left, right = map(int, data[index].split('-'))
    added = portion.closed(left, right)
    new_fresh_interval_set |=  added
    index += 1
# print(new_fresh_interval_set)

# for ID in range(new_fresh_interval_set.lower, new_fresh_interval_set.upper+1):
#     answer += (ID in new_fresh_interval_set)

for ID_range in new_fresh_interval_set:
    answer += ID_range.upper - ID_range.lower + 1
print(f'Part 2 : {answer}')