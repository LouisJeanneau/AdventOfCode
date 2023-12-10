import re

with open("2023_day09_input.txt") as f:
   data = [l.strip() for l in f.readlines()]

# data = open('2023_day09_sample.txt', 'r').read()
print("input = ", data)

# Part 1
def derivate(list):
   r = (len(list)-1)*[0]
   for ind in range(len(list)-1):
      r[ind] = list[ind+1] - list[ind]
   return r

answer = 0
for line in data:
   numbers = [int(i) for i in re.findall(r"-?\d+", line)]
   derivatives = [numbers.copy()]
   while derivatives[-1].count(0) != len(derivatives[-1]):
      derivatives.append( derivate(derivatives[-1]) )
   for i in range(len(derivatives)-1, 0, -1):
      derivatives[i-1].append(derivatives[i-1][-1] + derivatives[i][-1])
   print(derivatives[0][-1])
   answer += derivatives[0][-1]
print(answer)


# Part 2
print("#Part 2")
answer = 0
for line in data:
   numbers = [int(i) for i in re.findall(r"-?\d+", line)]
   derivatives = [numbers.copy()]
   while derivatives[-1].count(0) != len(derivatives[-1]):
      derivatives.append( derivate(derivatives[-1]) )
   for i in range(len(derivatives)-1, 0, -1):
      derivatives[i-1].insert(0, derivatives[i-1][0] - derivatives[i][0])
   print(derivatives[0][0])
   answer += derivatives[0][0]
print(answer)
# 19737 too high
