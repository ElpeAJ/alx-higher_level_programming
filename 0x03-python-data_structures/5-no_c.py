#!/usr/bin/python3

def no_c(my_string):
    new_characters = []
    for i in my_string:
        if i.lower() not in {'c', 'C'}:
            new_characters.append(i)
    new_string = ''.join(new_characters)
    return (new_string)
