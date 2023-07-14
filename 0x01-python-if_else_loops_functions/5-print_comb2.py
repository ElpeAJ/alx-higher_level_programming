#!/usr/bin/python3

numbers = range(0, 100, 1)

for i in numbers:
    if i < 99:
        print("{:02d}, ".format(i), end="")
        continue
    print(i)
