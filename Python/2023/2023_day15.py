with open("2023_day15_input.txt") as f:
# with open("2023_day15_sample.txt") as f:
   data = [l.strip() for l in f.readlines()]



print("input = ", data)

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
label = ""
lensNumber = 0
boxes = dict()
for operations in data[0].split(","):
    # print(operations)
    if '-' in operations:
        label = operations.split("-")[0]
        h = hash(label)
        box = boxes.get(h, [])
        for lens in box:
            if lens[0] == label:
                box.remove(lens)
        boxes[h] = box
    else:
        label, lensNumber = operations.split("=")
        h = hash(label)
        box = boxes.get(h, [])
        skip = False
        for index, lens in enumerate(box):
            if lens[0] == label:
                box[index] = (label, lensNumber)
                skip = True
                break
        if not skip:
            box.append((label, lensNumber))
        boxes[h] = box
    # print(label, lensNumber)
print(boxes)
total = 0
for k,v in boxes.items():
    for index, box in enumerate(v):
        total += (k+1)*(index+1)*int(box[1])
print(total)