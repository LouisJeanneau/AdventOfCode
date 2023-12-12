import datetime
import os
import shutil
import string
from Python.fetch_input import fetchOnline

for i in range(1, datetime.datetime.now().day + 1):
    # shutil.move(f'me_day{i}.py', f'day{i:0>2}/')
    # shutil.move(f'GPT_day{i}.py', f'day{i:0>2}/')

    # f = os.mkdir(f'2015/day{i:0>2}')
    # f = open(f'2015/day{i:0>2}/demo.txt', "w")
    # f.close()
    # os.remove(f'2023/2023_{i:0>2}day{i:0>2}.py')
    # os.remove(f'2023/2023_{i:0>2}day{i:0>2}_sample.txt')
    # os.remove(f'2023/2023_{i:0>2}day{i:0>2}_input.txt')

    # f = open(f'2023/2023_day{i:0>2}.py', "w")

    # f.write( str.format("with open(\"2023_day{i:0>2}_input.txt\") as f:\n", i=i) +
    #         "   data = [l.strip() for l in f.readlines()]\n\n" +
    #         str.format("# data = open('2023_day{i:0>2}_sample.txt', 'r').read()\n\n", i=i) +
    #         "print(\"input = \", data)\n\n" +
    #         "# Part 1\n" +
    #         "print(data)\n\n" +
    #         "# Part 2\n")
    # f.close()
    #
    # f = open(f'2023/2023_day{i:0>2}_sample.txt', "w")
    # f.close()

    f = open(f'2023/2023_day{i:0>2}_input.txt', "w")
    f.write(fetchOnline(2023, i))

    # shutil.copyfile(f'2015/day{i:0>2}/me_day{i:0>2}.py', f'2015/day{i:0>2}/me_2015_{i:0>2}.py')
    # os.remove(f'2015/day{i:0>2}/me_2015{i:0>2}.py')