import numpy as np

with open("2023_day13_sample.txt") as f:
# with open("2023_day13_input.txt") as f:
   data = [l.strip() for l in f.readlines()]
   data.append("")



# data = open('2023_day13_sample.txt', 'r').read()

print("input = ", data)

# Part 1
startMap = 0
total = 0
mapCount = 0
while data[startMap:].count(""):
   mapCount += 1
   print("mapCount = ", mapCount)
   endMap = data[startMap:].index("")+startMap
   map = np.array(data[startMap:endMap])
   startMap = endMap + 1
   # vertical scan
   for x in range(1, len(map)):
      cont = True
      for i in range(x):
         if 0<=x-1-i<len(map) and 0<=x+i<len(map):
            if map[x-1-i] != map[x+i]:
               cont = False
               break
         else:
            break
      if cont:
         print("Youhou")
         total += 100*x
         break

   tmap = map.T
   # horizontal scan
   for x in range(1, len(tmap)):
      cont = True
      for i in range(x):
         if 0<=x-1-i<len(tmap) and 0<=x+i<len(tmap):
            if tmap[x-1-i] != tmap[x+i]:
               cont = False
               break
         else:
            break
      if cont:
         print("Youhou")
         total += x
         break
print(total)
# 35299 too high
# Part 2
