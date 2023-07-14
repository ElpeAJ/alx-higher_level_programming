#!/usr/bin/python3

ascii_alphabet = range(97, 97 + 26, 1)
for i in ascii_alphabet:
    if (i == 101 or i == 113):
        continue
    print("{}".format(chr(i)), end="")
