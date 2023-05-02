from Python.fetch_input import fetchOnline

day = 11
'''
WATCH OUT FOR \n IN INPUT
'''
input = fetchOnline(2015, day).strip()
# input = open('demo.txt', 'r').read()
# input = "abcdefgh"
print("input = ", input)


# Part 1
def is_good(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    if not any(
            [chr(ord(password[i]) + 1) == password[i + 1] and chr(ord(password[i + 1]) + 1) == password[i + 2] for i in
             range(len(password) - 2)]):
        return False
    if len(set([password[i] for i in range(len(password) - 1) if password[i] == password[i + 1]])) < 2:
        return False
    return True

banned = ['i', 'o', 'l']

not_good = True
while not_good:
    for letter in banned:
        index = input.find(letter)
        if index != -1:
            input = input[:index] + chr(ord(letter) + 1) + 'a' * (len(input) - index - 1)

    carry = True
    my_index = -1
    while carry:
        carry = False
        l = list(input)
        value = ord(input[my_index])
        value += 1
        if value == 123:
            value = 97
            carry = True
        l[my_index] = chr(value)
        input = ''.join(l)
        if carry:
            my_index -= 1
    print("input = ", input)
    not_good = not is_good(input)

print("Part 1: ", input)
# Part 2 is using answer of part 1 as input
