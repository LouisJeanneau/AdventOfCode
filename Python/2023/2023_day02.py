colors = ("red", "green", "blue")
total = 0
inp = open("2023_day02_input.txt")
maxes = (12, 13, 14)

for id, line in enumerate(inp):
    # id = line[5:].split(":")[0]
    # print(id)
    sets = line.strip().split(":")[1].split(";")
    # print(sets)
    game = 3 * [0]
    # print(game)
    for set in sets:
        # print(set)
        set = set.strip()
        # print(set)
        for ball in set.split(","):
            ball = ball.strip()
            number, color = ball.split(" ")
            number = int(number)
            index = colors.index(color)
            if game[index] < number:
                game[index] = number

    # print(game)
    total += game[0] * game[1] * game[2]
print(total)
inp = open("2023_day02_input.txt")
total = 0
for id, line in enumerate(inp):
   # print(line)
   # id = line[5:].split(":")[0]
   # print(id)
   sets = line.strip().split(":")[1].split(";")
   # print(sets)
   valid = True
   for set in sets:
      # print(set)
      set = set.strip()
      # print(set)
      for ball in set.split(","):
         ball = ball.strip()
         # print(ball)
         number, color = ball.split(" ")
         # numb = ball
         # print(color)
         index = colors.index(color)
         # print(index)
         if int(number) > maxes[index]:
            valid = False
      # print(current)
   if valid:
      total += id + 1
      # print("good")
print(total)

