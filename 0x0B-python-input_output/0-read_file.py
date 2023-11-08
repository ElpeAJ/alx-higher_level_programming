#!/usr/bin/python3
"""A function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """Reads from file and prints to stdout"""

    with (open(filename, "r", encoding="UTF-8")) as f:
        print(f.read(), end="")
