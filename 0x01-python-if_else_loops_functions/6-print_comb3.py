#!/usr/bin/python3

step = 1
for i in range(9):
    for j in range(step, 10):
        if (i < 8 and j < 10):
            print("{}{}, ".format(i, j), end="")
            continue
        print("{}{}".format(i, j))
    step += 1
    j = range(step, 10)
