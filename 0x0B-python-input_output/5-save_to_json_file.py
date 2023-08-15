#!/usr/bin/python3
"""a function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ arguments: my_obj and filename as a str"""

    with open(filename, "w") as f:
        json.dumps(my_obj, f)
        #f.write(o_str)
