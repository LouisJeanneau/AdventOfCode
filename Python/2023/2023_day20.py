from collections import defaultdict
from collections import deque
from copy import deepcopy

# with open("2023_day20_sample.txt") as f:
with open("2023_day20_input.txt") as f:
    data = [l.strip().split(" -> ") for l in f.readlines()]

# Part 1
print("Part 1")
skeleton = {"type": "", "state": {}, "outputs": []}


def baseModule():
    return deepcopy(skeleton)


modules = defaultdict(baseModule)
print(data)


# Parse input
def parse():
    for module in [i for i in data if i[0][0] != '&']:
        if module[0] == "broadcaster":
            t = deepcopy(skeleton)
            t["type"] = module[0]
            t["outputs"] = [i.strip() for i in module[1].split(", ")]
            modules[module[0]] = t
        elif module[0][0] == "%":
            t = deepcopy(skeleton)
            name = module[0][1:]
            t["type"] = "flip"
            t["state"] = [False]
            outs = [i.strip() for i in module[1].split(", ")]
            t["outputs"] = outs
            for out in outs:
                dest = modules[out]
                if dest["type"] == "":
                    dest["state"][name] = False
            modules[name] = t
    for module in [i for i in data if i[0][0] == '&']:
        name = module[0][1:]
        t = modules[name]
        t["type"] = "conjuction"
        outs = [i.strip() for i in module[1].split(", ")]
        t["outputs"] = outs
        for out in outs:
            dest = modules[out]
            if dest["type"] == "conjuction" or dest["type"] == '':
                dest["state"][name] = False
        modules[name] = t


parse()
pulsesToTreat = deque()
total = {False: 0, True: 0}


def treatPulse(target, source, isHigh):
    total[isHigh] += 1
    if target == "output":
        return
    if target == "broadcaster":
        for t in modules[target]["outputs"]:
            pulsesToTreat.append((t, target, False))
    else:
        m = modules[target]
        if m["type"] == "flip" and not isHigh:
            s = m["state"][0]
            m["state"][0] = not s
            for t in modules[target]["outputs"]:
                pulsesToTreat.append((t, target, not s))
        elif m["type"] == "conjuction":
            m["state"][source] = isHigh
            state = [i[1] for i in m["state"].items()]
            whatToSend = False
            if False in state:
                whatToSend = True
            for t in modules[target]["outputs"]:
                pulsesToTreat.append((t, target, whatToSend))


for i in range(1000):
    pulsesToTreat.append(("broadcaster", "button", False))
    while pulsesToTreat:
        p = pulsesToTreat.popleft()
        if treatPulse(p[0], p[1], p[2]):
            print(f"PArt 2 : {i + 1}")
print(total)
print(f"part 1 : {total[0] * total[1]}")

# Part 2
print("Part 2")
i=0


def treatPulseAgain(target, source, isHigh):
    global i
    # manual finding of condition leading to rx receiving low
    if source in ("ln", "dr", "zx", "vn") and isHigh:
        print(i+1, source)
    if target == "output":
        return
    if target == "broadcaster":
        for t in modules[target]["outputs"]:
            pulsesToTreat.append((t, target, False))
    else:
        m = modules[target]
        if m["type"] == "flip" and not isHigh:
            s = m["state"][0]
            m["state"][0] = not s
            for t in modules[target]["outputs"]:
                pulsesToTreat.append((t, target, not s))
        elif m["type"] == "conjuction":
            m["state"][source] = isHigh
            state = [i[1] for i in m["state"].items()]
            whatToSend = False
            if False in state:
                whatToSend = True
            for t in modules[target]["outputs"]:
                pulsesToTreat.append((t, target, whatToSend))


parse()
for i in range(5000):
    pulsesToTreat.append(("broadcaster", "button", False))
    while pulsesToTreat:
        p = pulsesToTreat.popleft()
        treatPulseAgain(p[0], p[1], p[2])