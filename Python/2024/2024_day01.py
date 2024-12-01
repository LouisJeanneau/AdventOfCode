# with open("2024_day01_sample.txt") as f:
with open("2024_day01_input.txt") as f:
    data = [l.strip() for l in f.readlines()]

    left, right = [], []
    for line in data:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))

    sorted_left = sorted(left)
    sorted_right = sorted(right)
    ans = 0
    for i in range(len(sorted_left)):
        ans += abs(sorted_left[i] - sorted_right[i])

    print(ans)
    # Part 2
    ans = 0
    for i in range(len(sorted_left)):
        ans += sorted_left[i] * sorted_right.count(sorted_left[i])
    print(ans)