#!/usr/bin/python3
""" This file defines the ``append_after`` function """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file, after each line
    containing specific strings in a file.

    Parameters
    filename : string, optional
    search_string : string, optional
    new_string : string, optional
    """
    line_text = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line_text += line
            if (search_string in line):
                line_text += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(line_text)
