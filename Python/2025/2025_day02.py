
debug = False

if debug:
    with open("2025/2025_day02_sample.txt") as f:
        data = [l.strip() for l in f.readlines()]
else:
    with open("2025/2025_day02_input.txt") as f:
        data = [l.strip() for l in f.readlines()]

# Part 1
answer = 0
ranges = data[0].split(',')
for r in ranges:
    lower, upper = map(int, r.split('-'))
    for ID in range(lower, upper+1):
        ID_string = str(ID)
        ID_l=len(ID_string)
        if not ID_l % 2:
            # print(ID_string)
            # print(ID_string[0:ID_l//2],ID_string[ID_l//2:])
            if ID_string[0:ID_l//2]==ID_string[ID_l//2:]:
                answer += ID
print(f'Part 1 : {answer}')


# Part 2
answer = 0
for r in ranges:
    lower, upper = map(int, r.split('-'))
    for ID in range(lower, upper+1):
        ID_string = str(ID)
        ID_l=len(ID_string)
        for block_size in range(1,ID_l//2+1):
            if not ID_l % block_size:
                chunks = [ID_string[i:i+block_size] for i in range(0, ID_l, block_size)]
                if len(set(chunks)) == 1:
                    answer+=ID
                    break
print(f'Part 2 : {answer}')