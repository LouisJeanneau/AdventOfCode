from Python.fetch_input import fetchOnline

day = 10
input = fetchOnline(2015, day)
# input = open('demo.txt', 'r').read()

print("input = ", input)
input = input.strip()
# Part 1
def look_and_say(s):
    result = ""
    i = 0
    while i < len(s):
        c = s[i]
        count = 1
        while i + 1 < len(s) and s[i + 1] == c:
            count += 1
            i += 1
        result += str(count) + c
        i += 1
    return result

for i in range(40):
    input = look_and_say(input)
print("Part 1: ", len(input))

# Part 2
for i in range(10):
    input = look_and_say(input)
print("Part 2: ", len(input))