#!/usr/bin/python3
"""A script that adds all arguments to a
Python list, and then save them to a file"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items(args):
    try:
        py_list = load_from_json_file("add_item.json")
    except:
        py_list = []
    py_list += args
    save_to_json_file(py_list, "add_item.json")

    if __name__ == "__main__":
        add_item(sys.argv[1:])
