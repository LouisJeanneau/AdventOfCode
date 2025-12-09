import datetime
import os
import shutil
import string
import fetch_input

dir_path = os.path.dirname(os.path.realpath(__file__))
for i in range(8,9):
    # Py file
    try:
        with open(f'{dir_path}/2025/2025_day{i:0>2}.py', "x") as f:
            f.write("""
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

debug = False

if debug:
    with open(f'{dir_path}/2025/2025_""")
            f.write(f'day{i:0>2}_sample.txt\') as f:')
            f.write("""
        data = [l.strip('\\n') for l in f.readlines()]
else:
    with open(f'{dir_path}/2025_""")
            f.write(f'day{i:0>2}_input.txt\') as f:')
            f.write("""
        data = [l.strip('\\n') for l in f.readlines()]

# Part 1
answer = 0


print(f'Part 1 : {answer}')

# Part 2
answer = 0


print(f'Part 2 : {answer}')""")
        
        with open(f'{dir_path}/2025/2025_day{i:0>2}_sample.txt', "x") as f:
            f.write("blablabla")
        
        with open(f'{dir_path}/2025/2025_day{i:0>2}_input.txt', "x") as f:
            f.write(fetch_input.fetchOnline(2025, i))
    except FileExistsError:
        print("Some files already existed")
        # Your error handling goes here