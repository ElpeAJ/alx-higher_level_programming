#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Argument: filename
    returns: decoded JSON object that was loaded"""
    with open(filename, "r") as f:
        return json.load(f)
