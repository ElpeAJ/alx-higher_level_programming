#!/usr/bin/python3


def multiple_returns(sentence):
    length_of_string = 0
    char_one = None

    length_of_string = len(sentence)
    if (length_of_string > 0):
        char_one = sentence[0]

    else:
        return (length_of_string, char_one)
