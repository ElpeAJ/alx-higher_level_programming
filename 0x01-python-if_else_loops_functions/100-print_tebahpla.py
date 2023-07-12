#!/usr/bin/python3

iterator = range(122, 96, -1)

for index in iterator:
    if (index % 2 == 1):
        index = index - 32
    print("{}".format(chr(index)), end="")
