with open("2023_day07_input.txt") as f:
    data = [l.strip() for l in f.readlines()]

cards = "23456789TJQKA"

handsBet = dict()
handsValue = dict()
for line in data:
    left, right = line.split(" ")
    left = left.strip()
    right = right.strip()
    handsBet[left] = right
    counts = [left.count(c) for c in cards]
    valueDifferentiate = 815730721*cards.find(left[0]) + 28561*cards.find(left[1]) + 169*cards.find(left[2]) + 13*cards.find(left[3]) + 1*cards.find(left[4])
    if counts.count(5) == 1:
        handsValue[left] = 90000000000 + valueDifferentiate
    elif counts.count(4) == 1:
        handsValue[left] = 80000000000 + valueDifferentiate
    elif counts.count(3) == 1 and counts.count(2) == 1:
        handsValue[left] = 70000000000 + valueDifferentiate
    elif counts.count(3) == 1:
        handsValue[left] = 40000000000 + valueDifferentiate
    elif counts.count(2) == 2:
        handsValue[left] = 30000000000 + valueDifferentiate
    elif counts.count(2) == 1:
        handsValue[left] = 20000000000 + valueDifferentiate
    else:
        handsValue[left] = valueDifferentiate

hands = list(handsBet.keys())
hands.sort(key=lambda x: handsValue[x])
print(hands)
answer = 0
for v, hand in enumerate(hands):
    answer += int(handsBet[hand])*(v+1)
print(answer)
# 250382695 too high
# 250372054 too high
# 250370104

# Part 2
cards = "J23456789TQKA"

handsBet.clear()
handsValue.clear()
for line in data:
    left, right = line.split(" ")
    left = left.strip()
    right = right.strip()
    handsBet[left] = right
    counts = [left.count(c) for c in cards[1:]]
    jokerCount = left.count("J")
    print(counts)
    ind = len(counts) - counts[::-1].index(max(counts)) -1
    counts[ ind ] += jokerCount
    print(counts)
    valueDifferentiate = 815730721*cards.find(left[0]) + 28561*cards.find(left[1]) + 169*cards.find(left[2]) + 13*cards.find(left[3]) + 1*cards.find(left[4])
    if counts.count(5) == 1:
        handsValue[left] = 90000000000 + valueDifferentiate
    elif counts.count(4) == 1:
        handsValue[left] = 80000000000 + valueDifferentiate
    elif counts.count(3) == 1 and counts.count(2) == 1:
        handsValue[left] = 70000000000 + valueDifferentiate
    elif counts.count(3) == 1:
        handsValue[left] = 40000000000 + valueDifferentiate
    elif counts.count(2) == 2:
        handsValue[left] = 30000000000 + valueDifferentiate
    elif counts.count(2) == 1:
        handsValue[left] = 20000000000 + valueDifferentiate
    else:
        handsValue[left] = valueDifferentiate

hands = list(handsBet.keys())
hands.sort(key=lambda x: handsValue[x])
print(hands)
answer = 0
for v, hand in enumerate(hands):
    answer += int(handsBet[hand])*(v+1)
print(answer)

