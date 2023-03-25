import os
import shutil
import string

for i in range(1, 26):
    # shutil.move(f'me_day{i}.py', f'day{i:0>2}/')
    # shutil.move(f'GPT_day{i}.py', f'day{i:0>2}/')

    # f = os.mkdir(f'2015/day{i:0>2}')
    # f = open(f'2015/day{i:0>2}/demo.txt', "w")
    # f.close()
    f = open(f'2015/day{i:0>2}/me_2015_{i:0>2}.py', "w")

    f.write("from Python.fetch_input import fetchOnline\n\n" +
            str.format("day = {i}\n", i=i) +
            "input = fetchOnline(2015, day)\n" +
            "# input = open('demo.txt', 'r').read()\n\n" +
            "print(\"input = \", input)\n\n" +
            "# Part 1\n" +
            "print(input)\n\n" +
            "# Part 2\n")

    # shutil.copyfile(f'2015/day{i:0>2}/me_day{i:0>2}.py', f'2015/day{i:0>2}/me_2015_{i:0>2}.py')
    # os.remove(f'2015/day{i:0>2}/me_2015{i:0>2}.py')