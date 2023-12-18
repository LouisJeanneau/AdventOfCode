with open("2023_day15_input.txt") as f:
# with open("2023_day15_sample.txt") as f:
   data = [l.strip() for l in f.readlines()]



# print("input = ", data)

# Part 1
def hash(s):
    r = 0
    for c in s:
       r += ord(c)
       r *= 17
       r %= 256
    return r

print(sum([hash(l) for l in data[0].split(",")]))


# Part 2
for operations in data[0].split(","):
    print(operations)
    # label =
